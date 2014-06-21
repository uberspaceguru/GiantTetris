import os


# This is a place holder for the real display driver
class Display():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.idx = 0
        self.MAX_X = 9
        self.MAX_Y = 20
        self.characters = {0: '|', 1: '/', 2: '-', 3: '\\'}

    def draw(self, input):
        #Pixel obj (x,y)(r,g,b)
        # array over serial (115200) of lit pixels

        if input == 'LEFT':
            if self.x != 0:
                self.x -= 1
        elif input == 'RIGHT':
            if self.x < self.MAX_X - 1:
                self.x += 1
        elif input == 'ROTATE':
            self.idx = (self.idx + 1) % 4
        else:
            pass

        line = '|'
        for i in range(0, self.MAX_X):
            if self.x == i:
                line += self.characters[self.idx]
            else:
                line += ' '

        if self.y == self.MAX_Y:
            self.y = 0
            os.system('cls')
        print line + '|'
        self.y += 1

