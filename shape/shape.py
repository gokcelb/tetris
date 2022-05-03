<<<<<<< Updated upstream
import abc
import random

class Shape(metaclass=abc.ABCMeta):
=======
from abc import ABC, abstractmethod
import random

class Shape(ABC):
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
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
=======
    def random_color(self):
        return Shape.COLORS[random.randint(0, len(Shape.COLORS) - 1)]

    @abstractmethod
    def coordinates(self):
        raise NotImplementedError

    # @abstractmethod
    # def rotatations(self):
    #     raise NotImplementedError

class Basic(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
>>>>>>> Stashed changes

    def coordinates(self):
        return [[0, 0], [self.sqsz, 0], [self.sqsz*2, 0], [self.sqsz*3, 0]]

    def rotations(self):
        pass

class SquareInMiddle(Shape):
<<<<<<< Updated upstream
    def __init__(self):
        super().__init__()
=======
    def __init__(self, square_size):
        super().__init__(square_size)
>>>>>>> Stashed changes

    def coordinates(self):
        return [[0, 0], [self.sqsz, 0], [self.sqsz*2, 0], [self.sqsz*3, 0]]

    def rotations(self):
        pass

class SquareOnLeft(Shape):
<<<<<<< Updated upstream
    def __init__(self):
        super().__init__()
=======
    def __init__(self, square_size):
        super().__init__(square_size)
>>>>>>> Stashed changes

    def coordinates(self):
        return [[0, 0], [self.sqsz, 0], [self.sqsz*2, 0], [0, self.sqsz]]

    def rotations(self):
        pass

class SquareOnRight(Shape):
<<<<<<< Updated upstream
    def __init__(self):
        super().__init__()
=======
    def __init__(self, square_size):
        super().__init__(square_size)
>>>>>>> Stashed changes

    def coordinates(self):
        return [[0, 0], [self.sqsz, 0], [self.sqsz*2, 0], [self.sqsz*2, self.sqsz]]

    def rotations(self):
        pass

class Zigzag(Shape):
<<<<<<< Updated upstream
    def __init__(self):
        super().__init__()
=======
    def __init__(self, square_size):
        super().__init__(square_size)
>>>>>>> Stashed changes

    def coordinates(self):
        return [[0, 0], [self.sqsz, 0], [self.sqsz, self.sqsz], [self.sqsz*2, self.sqsz]]

    def rotations(self):
        pass
