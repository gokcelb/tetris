from abc import ABC


class Shape(ABC):
    def __init__(self, square_size):
        self.sqsz = square_size
        self.curr_coord_list = [[0, 0] for _ in range(4)]
        self.curr_center = [0, 0]

    def rotate(self):
        """
        Rotate the shape 90 degrees clockwise around a center.
        """
        center_x, center_y = self.curr_center

        # substracting self.sqsz from the x axis compensates the shift between
        # the coordinates of one corner and the other in 90 degree rotation
        for i in range(len(self.curr_coord_list)):
            x, y = self.curr_coord_list[i]
            self.curr_coord_list[i] = [
                center_x + center_y - y - self.sqsz, center_y - center_x + x
            ]


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
