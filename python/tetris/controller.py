import zmq
from collections import deque


class Controller:
    def __init__(self):
        self.port = '5555'
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.RCVTIMEO = 100
        self.socket.bind('tcp://*:%s' % self.port)

        self.cmd_queue = deque()
        self.default_cmd = ''

    def set_default_cmd(self, cmd):
        self.default_cmd = cmd

    def get_next_cmd(self):
        try:
            self.cmd_queue.append(self.socket.recv())
        except zmq.ZMQError:
            self.cmd_queue.append(self.default_cmd)

        return self.cmd_queue.pop()
