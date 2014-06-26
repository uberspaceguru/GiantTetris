from display import Display
from controller import Controller

display = Display(10, 20)
controller = Controller()

led_x = 1
led_y = 20

while True:
    display.pixel_off(led_x, led_y)
    cmd = controller.get_next_cmd()
    if cmd == 'LEFT':
        if led_x != 1:
            led_x -= 1
    elif cmd == 'RIGHT':
        if led_x != 10:
            led_x += 1
    led_y += 1

    pixel_test = {'x': led_x, 'y': led_y, 'r': 1, 'g': 1, 'b': 1}
    display.pixel_on(pixel=pixel_test)
    display.draw()
