import pygame
import random
from shape.shape_generator import ShapeGenerator

BLACK = (0, 0, 0)

SCREEN_SIZE = (400, 500)

SQUARE_SIZE = 20
SQUARE_DIMENSIONS = [SQUARE_SIZE , SQUARE_SIZE]
STARTING_COORDINATES = [
    random.randrange(SQUARE_SIZE * 3, SCREEN_SIZE[0] - SQUARE_SIZE * 4, 20),
    SQUARE_SIZE * 3
]

def main():
    pygame.init()

    pygame.display.set_icon(pygame.image.load('tetris.png'))
    pygame.display.set_caption('TETRIS')

    screen = pygame.display.set_mode(SCREEN_SIZE)

    running = True

    shape = ShapeGenerator(STARTING_COORDINATES, SQUARE_SIZE).random_shape()
    coordinates_list = shape.coordinates()

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for coordinates in coordinates_list:
            pygame.draw.rect(screen, shape.color, (coordinates, SQUARE_DIMENSIONS))
            pygame.draw.rect(screen, BLACK, (coordinates, SQUARE_DIMENSIONS), 1)

        pygame.display.flip()

if __name__ == "__main__":
    main()
