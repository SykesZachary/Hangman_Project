### Constructing the pokemon ee
### 08.03.2021

import os
import pygame as pg
import random
import sys
import time

from pygame.locals import *

from hangman_Difficulty import Difficulty
from hangman_MainGameRun import hangman

# Initialisation
pg.init()

# Game directories set
main = os.path.abspath(os.getcwd())
oswald_font_dir = 'OswaldFont/'
pkmn_font_dir = 'pkmn_font/'

# Fonts used
oswald_regular = os.path.join(main, oswald_font_dir, 'Oswald-Regular.ttf')
oswald_medium = os.path.join(main, oswald_font_dir, 'Oswald-Medium.ttf')
pkmn_hollow = os.path.join(main, pkmn_font_dir, 'Pokemon Hollow.ttf')

# Clock set
clock = pg.time.Clock()

# Colour Set
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)

PIKA_YELLOW = (251, 202, 60)
PIKA_RED = (197, 32, 24)

# Surface dimensions
eeDISPLAY_w = 600
eeDISPLAY_h = 800

# Surface setup
eeDISPLAY = pg.display.set_mode((eeDISPLAY_w, eeDISPLAY_h))
pg.display.set_caption('Hangman!')

# Font sizes
smallText = pg.font.Font(oswald_regular, 20)
medText = pg.font.Font(oswald_regular, 35)
largeText = pg.font.Font(oswald_regular, 50)

ee_large_text = pg.font.Font(pkmn_hollow, 50)
ee_small_text = pg.font.Font(pkmn_hollow, 20)


# Font rendering
def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


def ee_flavour_screen():

    interim = True

    while interim:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        eeDISPLAY.fill(BLACK)
        TextSurf, TextRect = text_objects(
            'Oh...?', largeText, WHITE)
        TextRect.center = ((eeDISPLAY_w / 2), (eeDISPLAY_h / 2))
        eeDISPLAY.blit(TextSurf, TextRect)

        pg.display.update()

        time.sleep(2)

        eeDISPLAY.fill(PIKA_YELLOW)
        TextSurf, TextRect = text_objects('An easter egg!', ee_large_text, BLACK)
        TextRect.center = ((eeDISPLAY_w / 2), (eeDISPLAY_h / 2))
        eeDISPLAY.blit(TextSurf, TextRect)

        # Pikachu's cheeks
        pg.draw.circle(eeDISPLAY, PIKA_RED,
                       (95, 650), 50)
        pg.draw.circle(eeDISPLAY, PIKA_RED,
                       (510, 650), 50)

        pg.display.update()
        time.sleep(2)
        clock.tick(15)

        interim = False


def PKMN_ee():
    pkmnGuess = random.choice(Difficulty.ee_word_bank())
    pkmnGuess = pkmnGuess.lower()

    ee_flavour_screen()

    pkmn = True
    while pkmn:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        eeDISPLAY.fill(PIKA_YELLOW)

        # Gallows
        pg.draw.line(eeDISPLAY, BLACK, (50, 100),
                     (50, 400), 4)  # Main backbone
        pg.draw.line(eeDISPLAY, BLACK, (50, 100), (150, 100), 4)  # Top bar
        pg.draw.line(eeDISPLAY, BLACK, (150, 100),
                     (150, 150), 4)  # Hanging rope
        pg.draw.line(eeDISPLAY, BLACK, (50, 375),
                     (180, 375), 4)  # Bottom board
        pg.draw.line(eeDISPLAY, BLACK, (180, 375), (180, 400), 4)  # Supports

        # Incorrect guesses bank
        incorrect_caption_box = pg.draw.rect(
            eeDISPLAY, PIKA_YELLOW, (355, 55, 200, 40))
        incorrect_guess = ee_small_text.render('Incorrect Guesses', True, BLACK)
        pg.draw.line(eeDISPLAY, BLACK, (340, 100), (560, 100), 4)
        eeDISPLAY.blit(incorrect_guess, incorrect_caption_box)

        # Pikachu's cheeks
        pg.draw.circle(eeDISPLAY, PIKA_RED,
                       (95, 650), 50)
        pg.draw.circle(eeDISPLAY, PIKA_RED,
                       (510, 650), 50)

        pg.display.update()
        clock.tick(15)
        pkmn = False

        hangman(pkmnGuess, 10, BLACK, PIKA_YELLOW)
