### This is just a test display to identify even output
### 29.01.2021

import pygame as pg
import sys

from pygame.locals import *
from time import sleep

# Initialisation
pg.init()

# Clock set
clock = pg.time.Clock()

# Display set
testDISPLAY = pg.display.set_mode((600, 800))  # Change depending on current project display size
pg.display.set_caption('Test Display')


def key_input():
    while True:
        events = pg.event.get()
        for event in events:
            if event.type == KEYDOWN:
                if event.key in code_list:
                    print(event.key)
                elif event.key not in code_list:
                    print('Invalid guess')
            if event.type == QUIT:
                pg.quit()
                sys.exit()


# Run Display
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

    testDISPLAY.fill((255, 255, 255))

    mouse_pos = pg.mouse.get_pos()
    mouse_click = pg.mouse.get_pressed()
    key_press = pg.key.get_pressed()

    # Hangman test
    alpha_dict = {'a': K_a, 'b': K_b, 'c': K_c, 'd': K_d, 'e': K_e, 'f': K_f, 'g': K_g,
                  'h': K_h, 'i': K_i, 'j': K_j, 'k': K_k, 'l': K_l, 'm': K_m, 'n': K_n,
                  'o': K_o, 'p': K_p, 'q': K_q, 'r': K_r, 's': K_s, 't': K_t, 'u': K_u,
                  'v': K_v, 'w': K_w, 'x': K_x, 'y': K_y, 'z': K_z}

    code_list = []
    word = 'coffee'

    for letter in list(word):
        code_list.append(alpha_dict[letter])

    key_input()

    pg.display.update()
    clock.tick(15)
