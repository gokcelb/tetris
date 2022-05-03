import random
<<<<<<< Updated upstream
import shape

class ShapeGenerator:
    def __init__(self, square_size):
        self.shapes = [
            shape.Basic(square_size),
            shape.SquareInMiddle(square_size),
            shape.SquareOnLeft(square_size),
            shape.SquareOnRight(square_size),
            shape.Zigzag(square_size)
        ]

    def random_shape(self) -> shape.Shape:
        return self.shapes[random.randint(0, len(self.shapes) - 1)]
=======
from shape.shape import Shape, Basic, SquareInMiddle, SquareOnLeft, SquareOnRight, Zigzag

class ShapeGenerator:
    def __init__(self, square_size):
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
        return shape(self.sqsz)
>>>>>>> Stashed changes
