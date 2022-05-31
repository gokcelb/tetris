from __future__ import annotations
from abc import ABC


class Shape(ABC):
    def __init__(self, square_size):
        self.sqsz = square_size
        self.color = None
        self.curr_coord_list = [[0, 0] for _ in range(4)]
        self.curr_center = [0, 0]
        self.on_ground = False
        self.mass = self.sqsz / 4

    def rotate(self):
        """Rotate the shape 90 degrees clockwise around a center."""
        center_x, center_y = self.curr_center

        # substracting self.sqsz from the x axis compensates the shift between
        # the coordinates of one corner and the other in 90 degree rotation
        for i in range(len(self.curr_coord_list)):
            x, y = self.curr_coord_list[i]
            self.curr_coord_list[i] = [
                center_x + center_y - y, center_y - center_x + x
            ]

    def clone(self) -> Shape:
        shape = Shape(self.sqsz)
        shape.curr_coord_list = self.curr_coord_list.copy()
        shape.curr_center = self.curr_center.copy()
        shape.on_ground = self.on_ground
        shape.color = self.color
        return shape

    def move(self, direction, unit):
        """
        Move to given direction for given unit distance.

        :param string direction: The direction towards which the shape will move.
        It can only be right or left.
        :param int unit: How many pixels the shape will move.
        """
        if direction == 'right':
            for coord in self.curr_coord_list:
                coord[0] += unit
            self.curr_center[0] += unit
        else:
            for coord in self.curr_coord_list:
                coord[0] -= unit
            self.curr_center[0] -= unit


class Basic(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0],
                                [self.sqsz * 2, 0], [self.sqsz * 3, 0]]
        self.center = [self.sqsz * 2, 0]


class SquareInMiddle(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0],
                                [self.sqsz * 2, 0], [self.sqsz, self.sqsz]]
        self.center = [self.sqsz, self.sqsz]


class SquareOnLeft(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0],
                                [self.sqsz * 2, 0], [0, self.sqsz]]
        self.center = [self.sqsz, self.sqsz]


class SquareOnRight(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0], [
            self.sqsz * 2, 0], [self.sqsz * 2, self.sqsz]]
        self.center = [self.sqsz, self.sqsz]


class Zigzag(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0], [
            self.sqsz, self.sqsz], [self.sqsz * 2, self.sqsz]]
        self.center = [self.sqsz, self.sqsz]


class Square(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0],
                                [0, self.sqsz], [self.sqsz, self.sqsz]]
        self.center = [self.sqsz, self.sqsz]
