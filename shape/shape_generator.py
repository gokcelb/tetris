import random
from shape.shape import Shape, Basic, SquareInMiddle, SquareOnLeft, SquareOnRight, Zigzag

class ShapeGenerator:
    def __init__(self, starting_coordinates, square_size):
        self.sc = starting_coordinates
        self.sqsz = square_size
        self.shapes = [
            Basic,
            SquareInMiddle,
            SquareOnLeft,
            SquareOnRight,
            Zigzag
        ]

    def random_shape(self) -> Shape:
        shape = self.shapes[random.randint(0, len(self.shapes) - 1)]
        return shape(self.sc, self.sqsz)
