import os


def draw_serial(data):
    os.system('cls')
    line = ''
    for val in data:
        line += '%x ' % ord(val)
    line += '\n'
    print line


def test_screen(pixels):
    os.system('cls')
    line = ''
    for i in xrange(20, 0, -1):
        for j in xrange(1, 11, 1):
            cell = pixels.get(str(hash_pixel(j, i)), None)
            if cell is not None:
                line += 'X '
            else:
                line += 'O '

        print line
        line = ''


def hash_pixel(x, y):
    return x + ((y - 1) * 10)


def send(data):
    print line

if __name__ == '__main__':
    pixel = {'x': 1, 'y': 200}
    send(pixel)