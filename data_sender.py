import socket
import pickle

class DataSender:
    def __init__(self, host='localhost', port=7500):
        self.host = host
        self.port = port

    def send_data(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(pickle.dumps(data))

# Usage example
if __name__ == "__main__":
    sender = DataSender()
    velocity = 30  # Example velocity
    throttle = 0.5  # Example throttle
    sender.send_data((velocity, throttle))
