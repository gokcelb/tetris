import pygame
from shape import ShapeGenerator

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
LIGHT_BLUE = (0, 255, 255)

UP = 'UP'
DOWN = 'DOWN'
RIGHT = 'RIGHT'
LEFT = 'LEFT'

UNIT = 15

SQUARE_SIZE = 15
SQUARE_DIMENSIONS = [SQUARE_SIZE , SQUARE_SIZE]

SCREEN_SIZE = (400, 500)


def main():
    pygame.init()

    pygame.display.set_icon(pygame.image.load('tetris.png'))
    pygame.display.set_caption('TETRIS')

    screen = pygame.display.set_mode(SCREEN_SIZE)

    running = True

    shape = ShapeGenerator(SQUARE_SIZE)
    coordinates_list = shape.coordinates()

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for coordinates in coordinates_list:
            pygame.draw.rect(screen, LIGHT_BLUE, (coordinates, SQUARE_DIMENSIONS))
            pygame.draw.rect(screen, BLACK, (coordinates, SQUARE_DIMENSIONS), 1)

        pygame.display.flip()

def draw_square(screen, color, coordinates, dimensions):
    pygame.draw.rect(screen, color, (coordinates, dimensions))

def draw_square_border(screen, coordinates, dimensions):
    pygame.draw.rect(screen, BLACK, (coordinates, dimensions), 1)

if __name__ == "__main__":
    main()
