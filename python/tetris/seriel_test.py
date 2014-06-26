def draw_screen(pixels):
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