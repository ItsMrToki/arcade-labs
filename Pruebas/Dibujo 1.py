from random import randrange

import arcade
from arcade.color import AMAZON, WHITE

HEIGHT = 750
WIDTH = 1250

arcade.open_window(1250, 750, "example")
arcade.set_background_color(arcade.color.PALE_AQUA)
arcade.start_render()

for i in range(200):
    arcade.draw_circle_filled(randrange(0, WIDTH, 10), randrange(0, HEIGHT, 10), 5, WHITE)
arcade.draw_circle_filled(625, -1800, 2000, AMAZON, 300, 500)



arcade.finish_render()
arcade.run()