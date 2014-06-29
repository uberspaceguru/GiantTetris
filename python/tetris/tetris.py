from display import Display
from controller import Controller

display = Display(10, 20)
controller = Controller()

led_x = 1
led_y = 20

pixel = {'x': led_x, 'y': led_y, 'r': 1, 'g': 1, 'b': 1}
display.pixel_on(pixel=pixel)

run = True
while run:
    try:
        display.draw()

        display.pixel_off(led_x, led_y)
        cmd = controller.get_next_cmd()
        if cmd == 'LEFT':
            #print 'moving left'
            if led_x != 1:
                led_x -= 1
        elif cmd == 'RIGHT':
            #print 'moving right'
            if led_x != 10:
                led_x += 1
        elif cmd == 'ROTATE':
            pass

        led_y -= 1
        if led_y < 1:
            led_y = 20

        pixel_test = {'x': led_x, 'y': led_y, 'r': 1, 'g': 1, 'b': 1}
        display.pixel_on(pixel=pixel_test)

        # pixel_test2 = {'x': 10, 'y': 20, 'r': 1, 'g': 1, 'b': 1}
        # display.pixel_on(pixel=pixel_test2)

        #for i in xrange(1, 20):
        #    for j in xrange(1, 10):
        #        display.pixel_on(pixel={'x': j, 'y': i, 'r': 255, 'g': 255, 'b': 255})
    except KeyboardInterrupt:
        print 'User Interrupt, stopping'
        run = False
