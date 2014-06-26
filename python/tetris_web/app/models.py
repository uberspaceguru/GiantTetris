import zmq


class Sender():
    def __init__(self):
        self.port = '5555'
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.connect("tcp://localhost:%s" % self.port)

    def send(self, command):
        try:
            self.socket.send(command, flags=zmq.NOBLOCK)
        except zmq.ZMQError as e:
            pass