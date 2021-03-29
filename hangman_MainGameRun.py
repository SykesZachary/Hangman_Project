### Building the main hangman game
### 28.01.2021

"""

TODO: Implement the definition function
TODO: Create an executable out of this game
TODO: Place pokemon easter egg

"""

import os
import pygame as pg
import random
import re
import time
import sys

from pygame.locals import *

from hangman_Difficulty import Difficulty
from hangman_BodyParts import body_parts
from hangman_EndScreen import end_screen

# Initialise
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

PIKA_YELLOW = (251, 202, 60)
PIKA_RED = (197, 32, 24)

# Surface dimensions
mainDISPLAY_w = 600
mainDISPLAY_h = 800

# Surface setup
mainDISPLAY = pg.display.set_mode((mainDISPLAY_w, mainDISPLAY_h))
pg.display.set_caption('Hangman!')

# Alphabet keys for pygame
alpha_dict = {'a': K_a, 'b': K_b, 'c': K_c, 'd': K_d, 'e': K_e, 'f': K_f, 'g': K_g,
              'h': K_h, 'i': K_i, 'j': K_j, 'k': K_k, 'l': K_l, 'm': K_m, 'n': K_n,
              'o': K_o, 'p': K_p, 'q': K_q, 'r': K_r, 's': K_s, 't': K_t, 'u': K_u,
              'v': K_v, 'w': K_w, 'x': K_x, 'y': K_y, 'z': K_z}

# Font sizes
smallText = pg.font.Font(oswald_regular, 20)
medText = pg.font.Font(oswald_regular, 35)
largeText = pg.font.Font(oswald_regular, 50)


# Font rendering
def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()


# Key register
def key_input(lst1, lst2):
    while True:
        events = pg.event.get()
        for event in events:
            if event.type == KEYDOWN:
                if event.key in alpha_dict.values():
                    if event.key in lst2:
                        return 0
                    elif event.key in lst1 and event.key not in lst2:
                        return pg.key.name(event.key).upper(), True
                    elif event.key not in lst1 and event.key not in lst2:
                        return pg.key.name(event.key).upper(), False

            if event.type == QUIT:
                pg.quit()
                sys.exit()


# Hangman run
def hangman(word, diff, colour_1, colour_2):  # 1 = line/letter 2 = bkgrnd

    symbol_list = [':', '\'', '-', '.']
    code_list = []
    for letter in list(word):
        if letter in symbol_list or letter == ' ':
            continue
        elif letter not in symbol_list:
            code_list.append(alpha_dict[letter])

    # Variables set for use during hangman. Explanations inline
    player_score = []  # Letters in target word correctly guessed
    prev_guess = []  # List of all letters previously guessed
    wrong_guess = []  # List of all wrongly guessed letters
    # Will only hold seven items to determine incorrect guess placements (row 1)
    box_row_1 = []
    # Will only hold seven items to determine incorrect guess placements (row 2)
    box_row_2 = []
    turn = diff  # Total number of turns before game end. 10 for Easy, 6 for hard

    # Hangman Game Loop Begin
    man_hang = True
    while man_hang:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        # Letter spaces
        bar_x = 65
        box_x = 60

        bar_y = 550
        box_y = 510

        bar_len = 30
        box_len = 30

        # Store rects to place correct guess letters
        letter_rects = []

        # Correct letter screen placement setup
        for letter in word:

            if letter in symbol_list:
                symbol_rect = pg.draw.rect(mainDISPLAY, colour_2,
                                           (box_x, box_y, box_len, 10))
                symbol_rect = symbol_rect.center
                symbol_text = smallText.render(letter, True, colour_1)
                mainDISPLAY.blit(symbol_text, symbol_rect)

                bar_x += (bar_len + 10)
                box_x += (box_len + 10)

                pg.display.update()

            elif letter != ' ':
                letter_rects.append(pg.draw.rect(
                    mainDISPLAY, colour_2, (box_x, box_y, box_len, 10)))
                pg.draw.line(mainDISPLAY, colour_1, (bar_x, bar_y),
                             ((bar_x + bar_len), bar_y), 2)

                bar_x += (bar_len + 10)
                box_x += (box_len + 10)

                pg.display.update()

            elif letter == ' ':
                bar_x += (bar_len + 10)
                box_x += (box_len + 10)

                pg.display.update()

        # Correct guess
        guess = key_input(code_list, prev_guess)
        if guess[1] is True:

            # Letter placement
            correctGuess = smallText.render(guess[0], True, colour_1)

            let_pos = 0

            # Setting up win condition word with just letters
            win_cond = word.replace(' ', '')
            rx = re.compile('([:\'-.])')
            win_cond = rx.sub('', win_cond)

            win_cond = win_cond.upper()

            for letter in list(win_cond):

                if guess[0] == letter:
                    correctRect = letter_rects[let_pos]
                    correctRect = correctRect.center
                    mainDISPLAY.blit(correctGuess, correctRect)

                    pg.display.update()
                    clock.tick(15)

                let_pos += 1

            # Append guess to list of made guesses
            if guess[0] not in prev_guess:
                prev_guess.append(guess[0])
            else:
                continue

            # Append correct guess to list
            player_score.append(guess[0])

            # Conditional to check win conditions
            if len(player_score) == len(set(list(win_cond))) and turn is not 0:  # Game Won!

                end_screen('win', colour_1, colour_2, word)

                # TODO: Put a grats screen with the word definition
                man_hang = False

        # Incorrect guess
        elif guess[1] is False:

            if guess[0] not in prev_guess:
                prev_guess.append(guess[0])

            # Incorrect letter screen placement setup
            # Holds pg.rects that incorrect guesses will go in
            bad_guess_box_list = []

            # Initial box coords
            box_x_init = 330
            box_y = 115
            box_len = 30

            # Setting the wrong guesses on the screen
            if guess[0] not in wrong_guess:
                wrong_guess.append(guess[0])

                body_parts(len(wrong_guess), mainDISPLAY, colour_1)

                if len(box_row_1) < 8:
                    box_row_1.append(guess[0])
                else:
                    box_row_2.append(guess[0])

                for i in range(0, 1):

                    box_x_mod = box_x_init + (box_len * len(box_row_1))

                    if box_x_mod > 555:
                        box_x_mod = 360 + (box_len * len(box_row_2))
                        box_y = box_y + 30
                        bad_guess_box = pg.draw.rect(
                            mainDISPLAY, colour_2, (box_x_mod, box_y, box_len, 10))
                        bad_guess_box_list.append(bad_guess_box)

                    else:
                        bad_guess_box = pg.draw.rect(
                            mainDISPLAY, colour_2, (box_x_mod, box_y, box_len, 10))
                        bad_guess_box_list.append(bad_guess_box)

                    bad_guess_text = smallText.render(
                        wrong_guess[-1], True, colour_1)
                    mainDISPLAY.blit(bad_guess_text, bad_guess_box_list[-1])

                    pg.display.update()
                    clock.tick(15)

                turn -= 1

            if turn == 0:  # Game is lost

                end_screen('loss', colour_1, colour_2, word)

                man_hang = False

        elif guess == 0:  # Wont be displayed. CL only
            continue

        pg.display.update()
        clock.tick(15)


# Game start screen setup
def flavour_screen():
    # Wholly unnecessary screen that provides
    # an illusion of the game thinking up a word for the player

    interim = True

    while interim:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        mainDISPLAY.fill(BLACK)
        TextSurf, TextRect = text_objects(
            'Ok... Let me pick a word', largeText)
        TextRect.center = ((mainDISPLAY_w / 2), (mainDISPLAY_h / 2))
        mainDISPLAY.blit(TextSurf, TextRect)

        pg.display.update()

        time.sleep(2)

        mainDISPLAY.fill(BLACK)
        TextSurf, TextRect = text_objects('Got one!', largeText)
        TextRect.center = ((mainDISPLAY_w / 2), (mainDISPLAY_h / 2))
        mainDISPLAY.blit(TextSurf, TextRect)

        pg.display.update()
        time.sleep(1)
        clock.tick(15)

        interim = False


def easy_game():
    wordGuess = random.choice(Difficulty.easy_modify())
    wordGuess = wordGuess.lower()

    flavour_screen()

    easy = True
    while easy:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        mainDISPLAY.fill(BLACK)

        # Gallows
        pg.draw.line(mainDISPLAY, WHITE, (50, 100),
                     (50, 400), 4)  # Main backbone
        pg.draw.line(mainDISPLAY, WHITE, (50, 100), (150, 100), 4)  # Top bar
        pg.draw.line(mainDISPLAY, WHITE, (150, 100),
                     (150, 150), 4)  # Hanging rope
        pg.draw.line(mainDISPLAY, WHITE, (50, 375),
                     (180, 375), 4)  # Bottom board
        pg.draw.line(mainDISPLAY, WHITE, (180, 375), (180, 400), 4)  # Supports

        # Incorrect guesses bank
        incorrect_caption_box = pg.draw.rect(
            mainDISPLAY, BLACK, (385, 55, 200, 40))
        incorrect_guess = smallText.render('Incorrect Guesses', True, WHITE)
        pg.draw.line(mainDISPLAY, WHITE, (340, 100), (560, 100), 4)
        mainDISPLAY.blit(incorrect_guess, incorrect_caption_box)

        pg.display.update()
        clock.tick(15)
        easy = False

    hangman(wordGuess, 10, WHITE, BLACK)


def hard_game():
    wordGuess = random.choice(Difficulty.hard_modify())
    wordGuess = wordGuess.lower()

    flavour_screen()

    hard = True
    while hard:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        mainDISPLAY.fill(BLACK)

        # Gallows
        pg.draw.line(mainDISPLAY, WHITE, (50, 100),
                     (50, 400), 4)  # Main backbone
        pg.draw.line(mainDISPLAY, WHITE, (50, 100), (150, 100), 4)  # Top bar
        pg.draw.line(mainDISPLAY, WHITE, (150, 100),
                     (150, 150), 4)  # Hanging rope
        pg.draw.line(mainDISPLAY, WHITE, (50, 375),
                     (180, 375), 4)  # Bottom board
        pg.draw.line(mainDISPLAY, WHITE, (180, 375), (180, 400), 4)  # Supports

        # Incorrect guesses bank
        incorrect_caption_box = pg.draw.rect(
            mainDISPLAY, BLACK, (385, 55, 200, 40))
        incorrect_guess = smallText.render('Incorrect Guesses', True, WHITE)
        pg.draw.line(mainDISPLAY, WHITE, (340, 100), (560, 100), 4)
        mainDISPLAY.blit(incorrect_guess, incorrect_caption_box)

        pg.display.update()
        clock.tick(15)
        hard = False

    hangman(wordGuess, 6, WHITE, BLACK)
