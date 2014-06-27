import seriel_test


class Display():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.on_pixels = dict()
        self.numPixels = width * height

    def draw(self):
        if self.on_pixels:
            seriel_test.draw_screen(self.on_pixels)

    def clear(self):
        self.on_pixels.clear()

    """ Provide a list of python dictionaries for each pixel to turn on """
    def set_scene(self, pixels=[]):
        """ Another way to clear the screen by calling with an empty list """
        if not pixels:
            self.clear()

    def pixel_on(self, pixel = dict()):
        if pixel:
            x = str(pixel.get('x', 0))
            y = str(pixel.get('y', 0))

            print 'Pixel On: ' + x + ', ' + y
            # If there is no x and y in the structure then it is invalid and ignore it
            if 0 != pixel.get('x', 0) and 0 != pixel.get('y', 0):
                # Add to on_pixels collection if color is provided
                if pixel.get('r', 0) or pixel.get('g', 0) or pixel.get('b', 0):
                    hashval = str(self.hash_pixel(pixel.get('x', 0), pixel.get('y', 0)))
                    self.on_pixels[hashval] = pixel

    def pixel_off(self, x, y):
        hashval = str(self.hash_pixel(x, y))
        if self.on_pixels.get(hashval, None) is not None:
            del self.on_pixels[hashval]
    
    def hash_pixel(self, x, y):
        return x + ((y - 1) * self.width)
