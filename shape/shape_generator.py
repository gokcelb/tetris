import random
from shape.shape import Shape, Basic, SquareInMiddle, SquareOnLeft, SquareOnRight, Zigzag


class ShapeGenerator:
    COLORS = [
        (255, 0, 0),
        (0, 0, 255),
        (0, 255, 0),
        (255, 255, 0),
        (255, 0, 255),
        (0, 255, 255)
    ]

    def __init__(self, starting_coord, square_size):
        self.starting_coord = starting_coord
        self.square_size = square_size
        self.shapes = [
            Basic,
            SquareInMiddle,
            SquareOnLeft,
            SquareOnRight,
            Zigzag
        ]
        self.shape = None

    def random_shape(self) -> Shape:
        shape = self.shapes[random.randint(0, len(self.shapes) - 1)]
        self.shape = shape(self.square_size)
        self.set_random_color()
        self.set_random_coordinates()
        return self.shape

    def set_random_color(self):
        self.shape.color = ShapeGenerator.COLORS[random.randint(
            0, len(ShapeGenerator.COLORS) - 1)]

    def set_random_coordinates(self):
        for i in range(len(self.shape.init_coord_list)):
            self.shape.curr_coord_list[i] = self.add_coordinates(
                self.starting_coord, self.shape.init_coord_list[i])

    @staticmethod
    def add_coordinates(first, second):
        return [a + b for a, b in zip(first, second)]
