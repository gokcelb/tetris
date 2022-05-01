import abc
import random

class Shape(metaclass=abc.ABCMeta):
    COLORS = [
        (255, 0, 0),
        (0, 0, 255),
        (0, 255, 0),
        (255, 255, 0),
        (255, 0, 255),
        (0, 255, 255)
    ]

    def __init__(self, square_size):
        self.sqsz = square_size
        self.color = self.random_color()

    @abc.abstractmethod
    def coordinates(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rotatations(self):
        raise NotImplementedError

    def random_color(self):
        return Shape.COLORS[random.randint(0, len(Shape.COLORS) - 1)]

class Basic(Shape):
    def __init__(self):
        super().__init__()

    def coordinates(self):
        return [[0, 0], [self.sqsz, 0], [self.sqsz*2, 0], [self.sqsz*3, 0]]

    def rotations(self):
        pass

class SquareInMiddle(Shape):
    def __init__(self):
        super().__init__()

    def coordinates(self):
        return [[0, 0], [self.sqsz, 0], [self.sqsz*2, 0], [self.sqsz*3, 0]]

    def rotations(self):
        pass

class SquareOnLeft(Shape):
    def __init__(self):
        super().__init__()

    def coordinates(self):
        return [[0, 0], [self.sqsz, 0], [self.sqsz*2, 0], [0, self.sqsz]]

    def rotations(self):
        pass

class SquareOnRight(Shape):
    def __init__(self):
        super().__init__()

    def coordinates(self):
        return [[0, 0], [self.sqsz, 0], [self.sqsz*2, 0], [self.sqsz*2, self.sqsz]]

    def rotations(self):
        pass

class Zigzag(Shape):
    def __init__(self):
        super().__init__()

    def coordinates(self):
        return [[0, 0], [self.sqsz, 0], [self.sqsz, self.sqsz], [self.sqsz*2, self.sqsz]]

    def rotations(self):
        pass
