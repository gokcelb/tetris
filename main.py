import pygame
import random
from shape.shape_generator import ShapeGenerator

BLACK = (0, 0, 0)

SCREEN_SIZE = (400, 500)

SQUARE_SIZE = 20
SQUARE_DIMENSIONS = [SQUARE_SIZE, SQUARE_SIZE]
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

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    shape.rotate()

        for coord in shape.curr_coord_list:
            draw(screen, shape.color, coord, SQUARE_DIMENSIONS)

        pygame.display.flip()


def draw(screen, color, coord, dimensions):
    pygame.draw.rect(screen, color, (coord, dimensions))
    pygame.draw.rect(screen, BLACK, (coord, dimensions), 1)


if __name__ == "__main__":
    main()
