from abc import ABC, abstractmethod
import random

class Shape(ABC):
    COLORS = [
        (255, 0, 0),
        (0, 0, 255),
        (0, 255, 0),
        (255, 255, 0),
        (255, 0, 255),
        (0, 255, 255)
    ]

    def __init__(self, starting_coordinates, square_size):
        self.sc = starting_coordinates
        self.sqsz = square_size
        self.color = self.random_color()

    def random_color(self):
        return Shape.COLORS[random.randint(0, len(Shape.COLORS) - 1)]

    @abstractmethod
    def coordinates(self):
        raise NotImplementedError

    # @abstractmethod
    # def rotatations(self):
    #     raise NotImplementedError

    @staticmethod
    def add_coordinates(first, second):
        return [a + b for a, b in zip(first, second)]

class Basic(Shape):
    def __init__(self, starting_coordinates, square_size):
        super().__init__(starting_coordinates, square_size)

    def coordinates(self):
        return [
            self.add_coordinates(self.sc, [0, 0]),
            self.add_coordinates(self.sc, [self.sqsz, 0]),
            self.add_coordinates(self.sc, [self.sqsz * 2, 0]),
            self.add_coordinates(self.sc, [self.sqsz * 3, 0])
            ]

    def rotations(self):
        pass

class SquareInMiddle(Shape):
    def __init__(self, starting_coordinates, square_size):
        super().__init__(starting_coordinates, square_size)

    def coordinates(self):
        return [
            self.add_coordinates(self.sc, [0, 0]),
            self.add_coordinates(self.sc, [self.sqsz, 0]),
            self.add_coordinates(self.sc, [self.sqsz * 2, 0]),
            self.add_coordinates(self.sc, [self.sqsz * 3, 0])
        ]

    def rotations(self):
        pass

class SquareOnLeft(Shape):
    def __init__(self, starting_coordinates, square_size):
        super().__init__(starting_coordinates, square_size)

    def coordinates(self):
        return [
            self.add_coordinates(self.sc, [0, 0]),
            self.add_coordinates(self.sc, [self.sqsz, 0]),
            self.add_coordinates(self.sc, [self.sqsz * 2, 0]),
            self.add_coordinates(self.sc, [0, self.sqsz])
        ]

    def rotations(self):
        pass

class SquareOnRight(Shape):
    def __init__(self, starting_coordinates, square_size):
        super().__init__(starting_coordinates, square_size)

    def coordinates(self):
        return [
            self.add_coordinates(self.sc, [0, 0]),
            self.add_coordinates(self.sc, [self.sqsz, 0]),
            self.add_coordinates(self.sc, [self.sqsz * 2, 0]),
            self.add_coordinates(self.sc, [self.sqsz * 2, self.sqsz])
        ]

    def rotations(self):
        pass

class Zigzag(Shape):
    def __init__(self, starting_coordinates, square_size):
        super().__init__(starting_coordinates, square_size)

    def coordinates(self):
        return [
            self.add_coordinates(self.sc, [0, 0]),
            self.add_coordinates(self.sc, [self.sqsz, 0]),
            self.add_coordinates(self.sc, [self.sqsz, self.sqsz]),
            self.add_coordinates(self.sc, [self.sqsz * 2, self.sqsz])
        ]

    def rotations(self):
        pass
