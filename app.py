from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from atem_mini import AtemMini
from threading import Thread
import time

app = Flask(__name__)
socketio = SocketIO(app)
atem = None

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('set_ip')
def handle_set_ip(data):
    global atem
    ip_address = data.get('ip')
    atem = AtemMini(ip=ip_address)
    atem.connect_to_switcher()
    thread = Thread(target=atem_loop)
    thread.start()

def atem_loop():
    global atem
    while(True):
        atem.loop()
        time.sleep(0)

@socketio.on('button_click')
def handle_button_click(data):
    global atem
    button = data.get('button')
    if atem is not None:
        atem.send_program_preview(source=int(button))    

if __name__ == '__main__':
    # Use eventlet for asynchronous socket handling
    socketio.run(app, debug=True, host='0.0.0.0')
