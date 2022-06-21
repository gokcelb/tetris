import pygame
import random
from collider import NO_COLLISION, VERTICAL_COLLISION, CollisionDetector
from gravity import Gravity
from ground import Ground
from shape.shape_generator import ShapeGenerator

BLACK = (0, 0, 0)

SCREEN_DIM = (300, 400)
UNIT = 20
RIGHT = 'right'
LEFT = 'left'
DOWN = 'down'

SQUARE_SIZE = 20
SQUARE_DIMENSIONS = [SQUARE_SIZE, SQUARE_SIZE]
STARTING_COORD = [random.randrange(
    SQUARE_SIZE * 3, SCREEN_DIM[0] - SQUARE_SIZE * 4, 20), SQUARE_SIZE * 3]


def main():
    pygame.init()
    pygame.display.set_icon(pygame.image.load('tetris.png'))
    pygame.display.set_caption('TETRIS')
    screen = pygame.display.set_mode(SCREEN_DIM)
    clock = pygame.time.Clock()

    running = True

    ground = Ground(SQUARE_SIZE, SCREEN_DIM)
    shape = ShapeGenerator(STARTING_COORD, SQUARE_SIZE).random_shape()

    collider = CollisionDetector(SCREEN_DIM)

    gravity = Gravity(collider)
    gravity.set_shape(shape).start()

    while running:
        clock.tick(10)

        screen.fill(BLACK)
        update_ground(ground, screen)

        update_shape(screen, shape)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    shape.rotate(SCREEN_DIM[0])
                elif event.key == pygame.K_RIGHT:
                    if collider.collision(shape, direction=-1) == NO_COLLISION and not is_at_border(shape, RIGHT):
                        shape.move(RIGHT, UNIT)
                elif event.key == pygame.K_LEFT:
                    if collider.collision(shape, direction=1) == NO_COLLISION and not is_at_border(shape, LEFT):
                        shape.move(LEFT, UNIT)
                elif event.key == pygame.K_DOWN:
                    if collider.collision(shape) == NO_COLLISION:
                        shape.move(DOWN, UNIT)

        if collider.collision(shape) == VERTICAL_COLLISION:
            add_shape_to_ground(ground, shape)
            ground.destroy_complete_rows()
            set_squares_on_ground_for_collider(collider, ground)

            del gravity
            del shape

            shape = ShapeGenerator(STARTING_COORD, SQUARE_SIZE).random_shape()

            gravity = Gravity(collider)
            gravity.set_shape(shape).start()

        pygame.display.flip()


def is_at_border(shape, direction: str) -> bool:
    for coord in shape.curr_coord_list:
        if direction == RIGHT and coord[0] + shape.sqsz == SCREEN_DIM[0]:
            return True
        if direction == LEFT and coord[0] == 0:
            return True
    return False


def set_squares_on_ground_for_collider(collider: CollisionDetector, ground: Ground) -> None:
    square_coords: list[list[int]] = []
    for square in ground.get_squares():
        square_coords.append(square['coord'])
    collider.set_square_coords(square_coords)


def add_shape_to_ground(ground: Ground, shape) -> None:
    for coord in shape.curr_coord_list:
        ground.add_square(coord, shape.color)


def update_ground(ground: Ground, screen) -> None:
    for square in ground.get_squares():
        update_square(screen, square['coord'], square['color'])


def update_shape(screen, shape) -> None:
    for coord in shape.curr_coord_list:
        update_square(screen, coord, shape.color)


def update_square(screen, coord, color) -> None:
    draw(screen, color, coord, SQUARE_DIMENSIONS)


def draw(screen, color, coord, dimensions) -> None:
    pygame.draw.rect(screen, color, (coord, dimensions))
    pygame.draw.rect(screen, BLACK, (coord, dimensions), 1)


if __name__ == "__main__":
    main()
