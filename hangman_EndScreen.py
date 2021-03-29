### Creating the end screen for the hangman game
### 08.03.2021

### Building the main hangman game
### 28.01.2021

"""

TODO: Implement the definition function
TODO: Create an executable out of this game

"""

import io
import os
import pygame as pg
import time
import sys

from pygame.locals import *
from urllib.request import Request, urlopen

from definition import Definition
from image_scraper import ImagePull


# Initialise
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
endDISPLAY_w = 600
endDISPLAY_h = 800

# Surface setup
endDISPLAY = pg.display.set_mode((endDISPLAY_w, endDISPLAY_h))
pg.display.set_caption('Hangman!')


# Font rendering
def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


def end_screen(cond, c1, c2, word):

    end = True
    while end:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        endDISPLAY.fill(c2)

        if c2 == PIKA_YELLOW:
            if cond == 'win':

                # Congratulaaaations https://tenor.com/brJVM.gif
                winText = pg.font.Font(oswald_regular, 50)
                winSurf, winRect = text_objects('Congratulations! You won!',
                                                winText, c1)
                winRect.center = ((endDISPLAY_w / 2), (endDISPLAY_h / 6))
                endDISPLAY.blit(winSurf, winRect)

                # This block capitalises the first letter in the word
                word = word.lower()
                word_lst = list(word)
                first_let = word_lst[0]
                first_let = first_let.upper()
                word_lst[0] = first_let
                word_reveal = ''

                for i in word_lst:
                    word_reveal += str(i)

                pkmn_reveal = ImagePull.pkmn_image_pull(word_reveal)

                # Display Pokémon national dex number
                pkmn_num = pg.font.Font(pkmn_hollow, 35)
                pkmn_num_surf, pkmn_num_rect = text_objects(pkmn_reveal[0],
                                                            pkmn_num, c1)
                pkmn_num_rect.center = ((endDISPLAY_w / 2), (endDISPLAY_h / 4))
                endDISPLAY.blit(pkmn_num_surf, pkmn_num_rect)

                # Display image of Pokémon
                req = Request(pkmn_reveal[1], headers={'User-Agent': 'Mozilla/5.0'})
                pkmn_image_str = urlopen(req).read()
                pkmn_image_file = io.BytesIO(pkmn_image_str)

                pkmn_image_load = pg.image.load(pkmn_image_file)
                endDISPLAY.blit(pkmn_image_load, (185, 300))

                # Pikachu's cheeks
                pg.draw.circle(endDISPLAY, PIKA_RED,
                               (95, 650), 50)
                pg.draw.circle(endDISPLAY, PIKA_RED,
                               (510, 650), 50)

                pg.display.update()
                clock.tick(15)

                time.sleep(3)

            elif cond == 'loss':

                lossText = pg.font.Font(oswald_regular, 50)
                lossSurf, lossRect = text_objects('Sorry, you lost.',
                                                  lossText, c1)
                lossRect.center = ((endDISPLAY_w / 2), (endDISPLAY_h / 6))
                endDISPLAY.blit(lossSurf, lossRect)

                time.sleep(1)

                # This block capitalises the first letter in the word
                word = word.lower()
                word_lst = list(word)
                first_let = word_lst[0]
                first_let = first_let.upper()
                word_lst[0] = first_let
                word_reveal = ''

                for i in word_lst:
                    word_reveal += str(i)

                # Prints the word missed on screen
                missed_text = pg.font.Font(oswald_regular, 35)
                missSurf, missRect = text_objects(f'The Pokémon was: {word_reveal}',
                                                  missed_text, c1)
                missRect.center = ((endDISPLAY_w / 2), (endDISPLAY_h / 4))
                endDISPLAY.blit(missSurf, missRect)

                pkmn_reveal = ImagePull.pkmn_image_pull(word_reveal)

                pkmn_num = pg.font.Font(pkmn_hollow, 35)
                pkmn_num_surf, pkmn_num_rect = text_objects(pkmn_reveal[0],
                                                            pkmn_num, c1)
                pkmn_num_rect.center = ((endDISPLAY_w / 2), (endDISPLAY_h / 3))
                endDISPLAY.blit(pkmn_num_surf, pkmn_num_rect)

                # Display image of Pokémon
                req = Request(pkmn_reveal[1], headers={'User-Agent': 'Mozilla/5.0'})
                pkmn_image_str = urlopen(req).read()
                pkmn_image_file = io.BytesIO(pkmn_image_str)

                pkmn_image_load = pg.image.load(pkmn_image_file)
                endDISPLAY.blit(pkmn_image_load, (185, 300))

                # Pikachu's cheeks
                pg.draw.circle(endDISPLAY, PIKA_RED,
                               (95, 650), 50)
                pg.draw.circle(endDISPLAY, PIKA_RED,
                               (510, 650), 50)

                pg.display.update()
                clock.tick(15)

                time.sleep(2)

        elif c2 == BLACK:
            if cond == 'win':

                # Congratulaaaations https://tenor.com/brJVM.gif
                winText = pg.font.Font(oswald_regular, 50)
                winSurf, winRect = text_objects('Congratulations! You won!',
                                                winText, c1)
                winRect.center = ((endDISPLAY_w / 2), (endDISPLAY_h / 5))
                endDISPLAY.blit(winSurf, winRect)

                Definition.definition_return(word)

                pg.display.update()
                clock.tick(15)

                time.sleep(3)

            elif cond == 'loss':

                lossText = pg.font.Font(oswald_regular, 50)
                lossSurf, lossRect = text_objects('Sorry, you lost.',
                                                  lossText, c1)
                lossRect.center = ((endDISPLAY_w / 2), (endDISPLAY_h / 6))
                endDISPLAY.blit(lossSurf, lossRect)

                time.sleep(1)

                # This block capitalises the first letter in the word
                word = word.lower()
                word_lst = list(word)
                first_let = word_lst[0]
                first_let = first_let.upper()
                word_lst[0] = first_let
                word_reveal = ''

                for i in word_lst:
                    word_reveal += str(i)

                # Prints the word missed on screen
                missed_text = pg.font.Font(oswald_regular, 35)
                missSurf, missRect = text_objects(f'The word was: {word_reveal}',
                                                  missed_text, c1)
                missRect.center = ((endDISPLAY_w / 2), (endDISPLAY_h / 4))
                endDISPLAY.blit(missSurf, missRect)

                pg.display.update()
                clock.tick(15)

                time.sleep(2)

                Definition.definition_return(word)

        end = False
