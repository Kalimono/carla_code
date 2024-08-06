import socket
import pickle
from pydub import AudioSegment
from pydub.playback import play

class DataReceiver:
    def __init__(self, host='localhost', port=7500):
        self.host = host
        self.port = port

    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Server listening on {self.host}:{self.port}")
            
            while True:
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    data = conn.recv(1024)
                    if not data:
                        break
                    velocity, throttle = pickle.loads(data)
                    print(f"Received data: velocity={velocity}, throttle={throttle}")
                    self.play_sound(throttle)

    def play_sound(self, throttle):
        if throttle < 0.3:
            sound = AudioSegment.from_wav("low_throttle.wav")
        elif throttle < 0.7:
            sound = AudioSegment.from_wav("medium_throttle.wav")
        else:
            sound = AudioSegment.from_wav("high_throttle.wav")
        
        play(sound)

# Usage example
if __name__ == "__main__":
    receiver = DataReceiver()
    receiver.start_server()
