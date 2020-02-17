import pygame, sys
from pygame.locals import *

pygame.init()

# TODO: Display an empty/dark screen done
# TODO: draw a square to the middle of a screen done
# TODO: the squre should be clickable done
# TODO: When the square is clicked, it disappears and a cat pops up done
# TODO: When the cat is clicked, it disappears and the square comes back up done
# TODO: Randomize getting the cat when clicking the card, i.e. player doesn't always get the cat upon clicking the card

DISPLAY_WIDTH = 600
DISPLAY_LENGTH = 400
SQUARE_LENGTH = 100
GAME_NAME = """Schrodinger's Cat"""
BG_COLOR = pygame.Color(255, 213, 90)
CARD_COLOR1 = pygame.Color(109, 212, 126)
CARD_COLOR2 = pygame.Color(41, 50, 80)
CAT_IMG_FILE = 'cat0.png'
TRANSPARENT = (0, 0, 0, 0)

showCat = False

DISPLAYSURF = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_LENGTH))
pygame.display.set_caption(GAME_NAME)
DISPLAYSURF.fill(BG_COLOR)

square = pygame.Rect(DISPLAY_WIDTH / 2 - SQUARE_LENGTH / 2, DISPLAY_LENGTH / 2 - SQUARE_LENGTH / 2, SQUARE_LENGTH, SQUARE_LENGTH)
pygame.draw.rect(DISPLAYSURF, CARD_COLOR1, square)
catImg = pygame.image.load(CAT_IMG_FILE)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()
            positionX = mousePosition[0]
            positionY = mousePosition[1]
            if (positionX >= DISPLAY_WIDTH / 2 - SQUARE_LENGTH / 2 and positionX <= DISPLAY_WIDTH / 2 + SQUARE_LENGTH / 2) and (positionY >= DISPLAY_LENGTH / 2 - SQUARE_LENGTH / 2 and positionY <= DISPLAY_LENGTH / 2 + SQUARE_LENGTH / 2):
                showCat = not showCat
                if (showCat):
                    print('B O O P !!')
                    pygame.draw.rect(DISPLAYSURF, BG_COLOR, square)
                    DISPLAYSURF.blit(catImg, (DISPLAY_WIDTH / 2 - SQUARE_LENGTH / 2, DISPLAY_LENGTH / 2 - SQUARE_LENGTH / 2))
                else:
                    print('Poopf!')
                    pygame.draw.rect(DISPLAYSURF, BG_COLOR, pygame.Rect(DISPLAY_WIDTH / 2 - SQUARE_LENGTH / 2, DISPLAY_LENGTH / 2 - SQUARE_LENGTH / 2, 122, SQUARE_LENGTH))
                    pygame.draw.rect(DISPLAYSURF, CARD_COLOR1, square)

    pygame.display.update()
