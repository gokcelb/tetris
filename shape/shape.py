from abc import ABC


class Shape(ABC):
    def __init__(self, square_size):
        self.sqsz = square_size
        self.curr_coord_list = [[0, 0] for _ in range(4)]

    def rotate(self):
        """
        Rotate the shape 90 degrees clockwise by updating shape coordinates.
        """
        # const_x and const_y are the coordinates of the square
        # that will always remain constant and unchanging
        const_x, const_y = self.curr_coord_list[0]

        for i in range(1, len(self.curr_coord_list)):
            x, y = self.curr_coord_list[i]
            self.curr_coord_list[i] = [const_x - y + const_y, const_y + x - const_x]

class Basic(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0],
                                [self.sqsz * 2, 0], [self.sqsz * 3, 0]]


class SquareInMiddle(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0],
                                [self.sqsz * 2, 0], [self.sqsz, self.sqsz]]


class SquareOnLeft(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0],
                                [self.sqsz * 2, 0], [0, self.sqsz]]


class SquareOnRight(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0], [
            self.sqsz * 2, 0], [self.sqsz * 2, self.sqsz]]


class Zigzag(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0], [
            self.sqsz, self.sqsz], [self.sqsz * 2, self.sqsz]]


class Square(Shape):
    def __init__(self, square_size):
        super().__init__(square_size)
        self.init_coord_list = [[0, 0], [self.sqsz, 0],
                                [0, self.sqsz], [self.sqsz, self.sqsz]]
