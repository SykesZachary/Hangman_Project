### Class to make a reusable button in pygame
### 01.28.2021

import pygame as pg


def button(surf, txt, x, y, w, h, c1, c2, c3,
           font, action=None):

    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    # Font rendering
    def text_objects(text, font):
        textSurface = font.render(text, True, c3)
        return textSurface, textSurface.get_rect()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pg.draw.rect(surf, c2, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()

    else:
        pg.draw.rect(surf, c1, (x, y, w, h))

    smallText = pg.font.Font(font, 20)
    buttonText, buttonRect = text_objects(txt, smallText)
    buttonRect.center = ((x + (w / 2)), (y + (h / 2)))
    surf.blit(buttonText, buttonRect)
