from pyatem.protocol import AtemProtocol
from pyatem.command import ProgramInputCommand, PreviewInputCommand, StreamingStatusSetCommand, RecorderStatusCommand
from pyatem.command import FairlightStripPropertiesCommand, AuxSourceCommand
import threading
import time

class AtemMini:
    def __init__(self, ip: str):
        self.switcher = AtemProtocol(ip)
        #self.connect_to_switcher()
        #thread = threading.Thread(target=self.loop)
        #thread.start()

    def connect_to_switcher(self):
        self.switcher.on('connected', self.on_connected)
        #self.switcher.on("change", self.on_change)
        self.switcher.connect()

    def on_change(self,a ,b):
        print(b)
        #pass
        
    def on_connected(self):
        print("Connection successful")
        #self.send_mic(source=1301, state=2)
        #self.send_mic(source=1302, state=2)
        #self.send_aux(source=10010)
        #self.send_program_preview(source=1)
            
    def send_program_preview(self, source):
        program = ProgramInputCommand(index=0, source=source)
        preview = PreviewInputCommand(index=0, source=source)
        self.switcher.send_commands([program, preview])
        #self.switcher.on("change", self.off_loop)

    def send_on_air(self, state):
        onAir = StreamingStatusSetCommand(streaming=state)
        self.switcher.send_commands([onAir])

    def send_record(self, state):
        Rec = RecorderStatusCommand(state)
        self.switcher.send_commands([Rec])

    def send_mic(self, source, state):
        Mic = FairlightStripPropertiesCommand(source=source, channel=-1, state=state)
        self.switcher.send_commands([Mic])

    def send_aux(self, source):  
        Aux = AuxSourceCommand(index=0, source=source)
        self.switcher.send_commands([Aux])

    def loop(self):
        #while(self.looping):
        self.switcher.loop()
        #    time.sleep(0.1)

    def off_loop(self):
        self.looping = False




def main():
  atem = AtemMini(ip="192.168.0.103")
  atem.connect_to_switcher()
  while(True):
    atem.loop()
  
  
 
if __name__ == "__main__":
  main()