import pygame
import random
import asyncio
from shape.shape_generator import ShapeGenerator

BLACK = (0, 0, 0)

SCREEN_DIMENSIONS = (400, 500)
GRAVITY = 8
UNIT = 20
RIGHT = 'right'
LEFT = 'left'

SQUARE_SIZE = 20
SQUARE_DIMENSIONS = [SQUARE_SIZE, SQUARE_SIZE]
STARTING_COORDINATES = [
    random.randrange(
        SQUARE_SIZE * 3, SCREEN_DIMENSIONS[0] - SQUARE_SIZE * 4, 20
    ), SQUARE_SIZE * 3
]


def main():
    pygame.init()
    pygame.display.set_icon(pygame.image.load('tetris.png'))
    pygame.display.set_caption('TETRIS')
    screen = pygame.display.set_mode(SCREEN_DIMENSIONS)

    running = True

    shape = ShapeGenerator(STARTING_COORDINATES, SQUARE_SIZE).random_shape()

    loop = asyncio.get_event_loop()
    loop.create_task(shape.fall(SCREEN_DIMENSIONS[1], GRAVITY))

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    shape.rotate()
                elif event.key == pygame.K_d:
                    shape.move(RIGHT, UNIT)
                elif event.key == pygame.K_a:
                    shape.move(LEFT, UNIT)

        for coord in shape.curr_coord_list:
            draw(screen, shape.color, coord, SQUARE_DIMENSIONS)
            pygame.draw.circle(screen, (155, 0, 255), shape.curr_center, 5)

        run_once(loop)

        pygame.display.flip()

    loop.close()


def draw(screen, color, coord, dimensions):
    pygame.draw.rect(screen, color, (coord, dimensions))
    pygame.draw.rect(screen, BLACK, (coord, dimensions), 1)


def run_once(loop):
    loop.call_soon(loop.stop)
    loop.run_forever()


if __name__ == "__main__":
    main()
