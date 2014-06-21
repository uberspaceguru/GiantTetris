import zmq
from display import Display

port = '5555'
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.RCVTIMEO = 1000
socket.connect('tcp://localhost:%s' % port)

display = Display()

while True:
    msg = 'DOWN'
    try:
        msg = socket.recv()
    except zmq.ZMQError:
        msg = 'DOWN'

    display.draw(msg)

socket.close()