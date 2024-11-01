from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from atem_mini import AtemMini
from threading import Thread
import time
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests
socketio = SocketIO(app)
atem = None

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('set_ip')
def handle_set_ip(data):
    global atem
    app.logger.debug(f"Received set_ip: {data}")
    ip_address = data.get('ip')
    atem = AtemMini(ip=ip_address)
    atem.connect_to_switcher()
    thread = Thread(target=atem_loop)
    thread.start()

def atem_loop():
    global atem
    while True:
        atem.loop()
        time.sleep(0.1)  # Adjust sleep to prevent high CPU usage

@socketio.on('button_click')
def handle_button_click(data):
    global atem
    app.logger.debug(f"Received button_click: {data}")
    button = data.get('button')
    if atem is not None:
        atem.send_program_preview(source=int(button))

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
