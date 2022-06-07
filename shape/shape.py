from __future__ import annotations
from abc import ABC


class Shape(ABC):
    def __init__(self, square_size):
        self.sqsz = square_size
        self.color = None
        self.curr_coord_list = [[0, 0] for _ in range(4)]
        self.curr_center = [0, 0]
        self.mass = self.sqsz / 4

    def rotate(self, screen_length: int) -> None:
        """Rotate the shape 90 degrees clockwise around a center."""
        center_x, center_y = self.curr_center

        for i in range(len(self.curr_coord_list)):
            x, y = self.curr_coord_list[i]
            new_x = center_x + center_y - y
            new_y = center_y - center_x + x

            if new_x < 0 or new_x + self.sqsz > screen_length:
                return
            self.curr_coord_list[i] = [new_x, new_y]

    def move(self, direction, unit) -> None:
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
        elif direction == 'left':
            for coord in self.curr_coord_list:
                coord[0] -= unit
            self.curr_center[0] -= unit
        elif direction == 'down':
            for coord in self.curr_coord_list:
                coord[1] += unit
            self.curr_center[1] += unit

    def clone(self) -> Shape:
        shape = Shape(self.sqsz)
        shape.curr_coord_list = self.curr_coord_list.copy()
        shape.curr_center = self.curr_center.copy()
        shape.color = self.color
        return shape


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

    def rotate(self, screen_length: int) -> None:
        return
