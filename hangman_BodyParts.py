### Body parts to add to the hangman's gallows
### 01.02.2021

import pygame as pg

# Initialise
pg.init()

# Clock set
clock = pg.time.Clock()


def body_parts(part, display, color):
    # The coordinates in this method are set to work with hangman_MainGameRun.py
    # TODO: Eventually draw a man chop it up and import the images

    if part == 1:  # Head

        pg.draw.circle(display, color, (150, 170), 20, 3)
        pg.display.update()
        clock.tick(15)

    elif part == 2:  # Body

        pg.draw.line(display, color, (150, 190), (150, 250), 3)
        pg.display.update()
        clock.tick(15)

    elif part == 3:  # Right arm

        pg.draw.line(display, color, (150, 195), (138, 225), 3)
        pg.display.update()
        clock.tick(15)

    elif part == 4:  # Left arm

        pg.draw.line(display, color, (150, 195), (162, 225), 3)
        pg.display.update()
        clock.tick(15)

    elif part == 5:  # Right leg

        pg.draw.line(display, color, (150, 250), (138, 285), 3)
        pg.display.update()
        clock.tick(15)

    elif part == 6:  # Left leg

        pg.draw.line(display, color, (150, 250), (162, 285), 3)
        pg.display.update()
        clock.tick(15)

    elif part == 7:  # Right hand

        pg.draw.circle(display, color, (137, 228), 4, 4)
        pg.display.update()
        clock.tick()

    elif part == 8:  # Left hand

        pg.draw.circle(display, color, (164, 228), 4, 4)
        pg.display.update()
        clock.tick()

    elif part == 9:  # Right foot

        right_foot = pg.draw.rect(display, (0, 0, 0), (132, 284, 7, 4))
        pg.draw.ellipse(display, color, right_foot, 4)
        pg.display.update()
        clock.tick()

    elif part == 10:  # Left foot

        left_foot = pg.draw.rect(display, (0, 0, 0), (161, 284, 7, 4))
        pg.draw.ellipse(display, color, left_foot, 4)
        pg.display.update()
        clock.tick()