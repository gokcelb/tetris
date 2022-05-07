from abc import ABC
import asyncio


class Shape(ABC):
    def __init__(self, square_size):
        self.sqsz = square_size
        self.curr_coord_list = [[0, 0] for _ in range(4)]
        self.curr_center = [0, 0]

    def rotate(self):
        """Rotate the shape 90 degrees clockwise around a center."""
        center_x, center_y = self.curr_center

        # substracting self.sqsz from the x axis compensates the shift between
        # the coordinates of one corner and the other in 90 degree rotation
        for i in range(len(self.curr_coord_list)):
            x, y = self.curr_coord_list[i]
            self.curr_coord_list[i] = [
                center_x + center_y - y - self.sqsz, center_y - center_x + x
            ]

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

    async def fall(self, screen_height, gravity):
        """
        Fall until screen length at a speed based on gravity.

        :param int screen_height: y axis of game screen
        :param int gravity: In-game gravity
        """
        mass = self.sqsz * 0.25
        while self.is_on_air(screen_height):
            await asyncio.sleep(0.5)

            fallable_height = self.fallable_height(screen_height)
            if fallable_height < mass * gravity:
                self.fall_for(fallable_height)
            else:
                self.fall_for(mass * gravity)

    def is_on_air(self, screen_height):
        for coord in self.curr_coord_list:
            if coord[1] == screen_height - self.sqsz:
                return False
        return True

    def fallable_height(self, screen_height):
        closest_to_ground = 0
        for coord in self.curr_coord_list:
            if coord[1] > closest_to_ground:
                closest_to_ground = coord[1]
        return screen_height - self.sqsz - closest_to_ground

    def fall_for(self, height):
        for coord in self.curr_coord_list:
            coord[1] += height
        self.curr_center[1] += height


class Basic(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0],
                                [self.sqsz * 2, 0], [self.sqsz * 3, 0]]
        self.center = [self.sqsz * 2, self.sqsz * 0.5]


class SquareInMiddle(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0],
                                [self.sqsz * 2, 0], [self.sqsz, self.sqsz]]
        self.center = [self.sqsz * 1.5, self.sqsz]


class SquareOnLeft(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0],
                                [self.sqsz * 2, 0], [0, self.sqsz]]
        self.center = [self.sqsz * 1.5, self.sqsz]


class SquareOnRight(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0], [
            self.sqsz * 2, 0], [self.sqsz * 2, self.sqsz]]
        self.center = [self.sqsz * 1.5, self.sqsz]


class Zigzag(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0], [
            self.sqsz, self.sqsz], [self.sqsz * 2, self.sqsz]]
        self.center = [self.sqsz * 1.5, self.sqsz]


class Square(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0],
                                [0, self.sqsz], [self.sqsz, self.sqsz]]
        self.center = [self.sqsz, self.sqsz]
