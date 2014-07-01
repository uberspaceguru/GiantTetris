from __future__ import print_function
import serial
import time

class Display():
    def __init__(self, width, height):
        # Some constants for the program
        self.START_OF_STREAM = '!'
        self.END_OF_STREAM = '\n'
        self.VALUE_SEPARATOR = ' '

        # serial port config
        self.SERIAL_COM_PORT = 'COM5'
        #self.SERIAL_COM_PORT = 'COM6'
        self.BAUD_RATE = 115200
        self.PARITY = serial.PARITY_NONE
        self.STOPBITS = serial.STOPBITS_ONE
        self.BYTESIZE = serial.EIGHTBITS

        self.width = width
        self.height = height
        self.on_pixels = dict()
        self.numPixels = width * height

        self.serialPort = serial.Serial(port=self.SERIAL_COM_PORT,
                                        baudrate=self.BAUD_RATE,
                                        parity=self.PARITY,
                                        stopbits=self.STOPBITS,
                                        bytesize=self.BYTESIZE)

        time.sleep(2)

        print('Program is running check serial port for output, using %s' % self.serialPort.portstr)

    def __del__(self):
        self.serialPort.close()

    def draw(self):
        if self.on_pixels:
            self.serial_send(self.START_OF_STREAM)
            for pixel in self.on_pixels:
                #self.serial_send(self.on_pixels[pixel].get('x', 0))
                self.serial_send(self.on_pixels[pixel]['x'])
                self.serial_send(self.VALUE_SEPARATOR)
                #self.serial_send(self.on_pixels[pixel].get('y', 0))
                self.serial_send(self.on_pixels[pixel]['y'])
                self.serial_send(self.VALUE_SEPARATOR)
                #self.serial_send(self.on_pixels[pixel].get('g', 0))
                self.serial_send(self.on_pixels[pixel]['r'])
                self.serial_send(self.VALUE_SEPARATOR)
                #self.serial_send(self.on_pixels[pixel].get('r', 0))
                self.serial_send(self.on_pixels[pixel]['g'])
                self.serial_send(self.VALUE_SEPARATOR)
                #self.serial_send(self.on_pixels[pixel].get('b', 0))
                self.serial_send(self.on_pixels[pixel]['b'])
                self.serial_send(self.VALUE_SEPARATOR)
            self.serial_send(self.END_OF_STREAM)

    def clear(self):
        self.on_pixels.clear()

    """ Provide a list of python dictionaries for each pixel to turn on """
    def set_scene(self, pixels=[]):
        """ Another way to clear the screen by calling with an empty list """
        self.clear()
        if pixels:
            for pixel in pixels:
                self.pixel_on(pixel)

    def pixel_on(self, pixel=dict()):
        if pixel:
            # If there is no x and y in the structure then it is invalid and ignore it
            if 0 <= pixel.get('x', 0) and 0 <= pixel.get('y', 0):
                # Add to on_pixels collection if color is provided
                if pixel.get('r', 0) or pixel.get('g', 0) or pixel.get('b', 0):
                    hashval = str(self.hash_pixel(pixel.get('x', 0), pixel.get('y', 0)))
                    self.on_pixels[hashval] = pixel

    def pixel_off(self, x, y):
        hashval = str(self.hash_pixel(x, y))
        if self.on_pixels.get(hashval, None) is not None:
            del self.on_pixels[hashval]

    def serial_send(self, data):
        try:
            self.serialPort.write(str(data))
        except TypeError:
            pass
            self.serialPort.write(data)

        if self.SERIAL_COM_PORT == 'COM6':
            print(self.serialPort.readline(), end='')

    def hash_pixel(self, x, y):
        #return x + ((y  - 1) * self.width)
        return x + (y * self.width)
