### Constructing the title screen
### 28.01.2021

import os
import pygame as pg
import sys

from pygame.locals import *

from pygameButton import button
from hangman_MainGameRun import easy_game
from hangman_MainGameRun import hard_game
from hangman_PKMNee import PKMN_ee


# Initialisation
pg.init()

# Game directories set
main = os.path.abspath(os.getcwd())
oswald_font_dir = 'OswaldFont/'

# Fonts used
oswald_regular = os.path.join(main, oswald_font_dir, 'Oswald-Regular.ttf')
oswald_medium = os.path.join(main, oswald_font_dir, 'Oswald-Medium.ttf')

# Clock set
clock = pg.time.Clock()

# Colour Set
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)

trans_BLACK = (0, 0, 0, 0)

PIKA_YELLOW = (251, 202, 60)
PIKA_RED = (197, 32, 24)

# Surface dimensions
titleDISPLAY_w = 600
titleDISPLAY_h = 800

# Surface setup
titleDISPLAY = pg.display.set_mode((titleDISPLAY_w, titleDISPLAY_h))
pg.display.set_caption('Hangman!')


# Font rendering
def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()


# Building difficulty select screen
def difficulty_select_screen():

    diffSelect = True

    while diffSelect:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        titleDISPLAY.fill(BLACK)
        largeText = pg.font.Font(oswald_medium, 50)
        TextSurf, TextRect = text_objects('Welcome to Hangman!', largeText)
        TextRect.center = ((titleDISPLAY_w / 2), (titleDISPLAY_h / 4))
        titleDISPLAY.blit(TextSurf, TextRect)

        medText = pg.font.Font(oswald_medium, 30)
        TextSurf, TextRect = text_objects('Please select your difficulty', medText)
        TextRect.center = ((titleDISPLAY_w / 2), (titleDISPLAY_h / 3))
        titleDISPLAY.blit(TextSurf, TextRect)

        # Easy diff select button
        pg.draw.rect(titleDISPLAY, WHITE, (145, 550, 110, 55))
        button(titleDISPLAY, 'Easy', 148, 553, 104, 50,
               BLACK, GREY, WHITE, oswald_regular, easy_game)

        # Hard diff select button
        pg.draw.rect(titleDISPLAY, WHITE, (355, 550, 110, 55))
        button(titleDISPLAY, 'Hard', 358, 553, 104, 50,
               BLACK, GREY, WHITE, oswald_regular, hard_game)

        # Back Button
        pg.draw.rect(titleDISPLAY, WHITE, (50, 695, 510, 55))
        button(titleDISPLAY, 'Back', 53, 698, 504, 50,
               BLACK, GREY, WHITE, oswald_regular, title_card)

        pg.display.update()
        clock.tick(15)


# Building title card
def title_card():

    intro = True

    while intro:
        for event in pg.event.get():
            # print(event)
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        titleDISPLAY.fill(BLACK)
        largeText = pg.font.Font(oswald_medium, 50)
        TextSurf, TextRect = text_objects('Welcome to Hangman!', largeText)
        TextRect.center = ((titleDISPLAY_w/2), (titleDISPLAY_h/4))
        titleDISPLAY.blit(TextSurf, TextRect)

        # Start Button
        pg.draw.rect(titleDISPLAY, WHITE, (145, 400, 110, 55))
        button(titleDISPLAY, 'Start', 148, 403, 104, 50,
               BLACK, GREEN, WHITE, oswald_regular, difficulty_select_screen)

        # Quit Button
        pg.draw.rect(titleDISPLAY, WHITE, (355, 400, 110, 55))
        button(titleDISPLAY, 'Quit', 358, 403, 104, 50,
               BLACK, RED, WHITE, oswald_regular, QUIT)
        # TODO: Calling QUIT above throws an error but it works.... fix later

        # Hidden PKMN EE call
        button(titleDISPLAY, '', 507, 215, 5, 5,
               WHITE, WHITE, WHITE, oswald_regular, PKMN_ee)

        pg.display.update()
        clock.tick(15)


# Run title screen
title_card()
