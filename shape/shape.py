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
        self.color = self.__random_color()

    def __random_color(self):
        return Shape.COLORS[random.randint(0, len(Shape.COLORS) - 1)]

    def coordinates(self):
        rotations = [0, 90, 180, 270]
        rotation_degree = rotations[random.randint(0, len(rotations) - 1)]
        if rotation_degree == 0:
            print('rotation degree is 0')
            return self.init_coordinates()

        return self.rotate(rotation_degree)

    def rotate(self, rotation_degree):
        init_coord = self.init_coordinates()
        origin = init_coord[0]
        rotated_coordinates_list = [origin]

        for i, coordinates in enumerate(init_coord):
            if i == 0:
                continue

            if rotation_degree == 90:
                new_coord = self.rotate_ninety(coordinates, origin)
            elif rotation_degree == 180:
                new_coord = self.rotate_one_hundred_eighty(coordinates, origin)
            elif rotation_degree == 270:
                new_coord = self.rotate_two_hundred_seventy(coordinates, origin)
            rotated_coordinates_list.append(new_coord)

        return rotated_coordinates_list

    def rotate_ninety(self, coordinates, origin):
        x = coordinates[0]
        y = coordinates[1]
        origin_x = origin[0]
        origin_y = origin[1]

        if y == origin_y:
            return [origin_x, origin_y + (x - origin_x)]
        elif y - origin_y == self.sqsz:
            return [origin_x - (y - origin_y), origin_y + (x - origin_x)]

    def rotate_one_hundred_eighty(self, coordinates, origin):
        x = coordinates[0]
        y = coordinates[1]
        origin_x = origin[0]

        return [origin_x - (x - origin_x), y]

    def rotate_two_hundred_seventy(self, coordinates, origin):
        new_coord = self.rotate_ninety(coordinates, origin)
        return self.rotate_one_hundred_eighty(new_coord, origin)

    @abstractmethod
    def init_coordinates(self):
        raise NotImplementedError

    @staticmethod
    def add_coordinates(first, second):
        return [a + b for a, b in zip(first, second)]

class Basic(Shape):
    def __init__(self, starting_coordinates, square_size):
        super().__init__(starting_coordinates, square_size)

    def init_coordinates(self):
        return [
            self.add_coordinates(self.sc, [0, 0]),
            self.add_coordinates(self.sc, [self.sqsz, 0]),
            self.add_coordinates(self.sc, [self.sqsz * 2, 0]),
            self.add_coordinates(self.sc, [self.sqsz * 3, 0])
            ]

class SquareInMiddle(Shape):
    def __init__(self, starting_coordinates, square_size):
        super().__init__(starting_coordinates, square_size)

    def init_coordinates(self):
        return [
            self.add_coordinates(self.sc, [0, 0]),
            self.add_coordinates(self.sc, [self.sqsz, 0]),
            self.add_coordinates(self.sc, [self.sqsz * 2, 0]),
            self.add_coordinates(self.sc, [self.sqsz, self.sqsz])
        ]

class SquareOnLeft(Shape):
    def __init__(self, starting_coordinates, square_size):
        super().__init__(starting_coordinates, square_size)

    def init_coordinates(self):
        return [
            self.add_coordinates(self.sc, [0, 0]),
            self.add_coordinates(self.sc, [self.sqsz, 0]),
            self.add_coordinates(self.sc, [self.sqsz * 2, 0]),
            self.add_coordinates(self.sc, [0, self.sqsz])
        ]

class SquareOnRight(Shape):
    def __init__(self, starting_coordinates, square_size):
        super().__init__(starting_coordinates, square_size)

    def init_coordinates(self):
        return [
            self.add_coordinates(self.sc, [0, 0]),
            self.add_coordinates(self.sc, [self.sqsz, 0]),
            self.add_coordinates(self.sc, [self.sqsz * 2, 0]),
            self.add_coordinates(self.sc, [self.sqsz * 2, self.sqsz])
        ]

class Zigzag(Shape):
    def __init__(self, starting_coordinates, square_size):
        super().__init__(starting_coordinates, square_size)

    def init_coordinates(self):
        return [
            self.add_coordinates(self.sc, [0, 0]),
            self.add_coordinates(self.sc, [self.sqsz, 0]),
            self.add_coordinates(self.sc, [self.sqsz, self.sqsz]),
            self.add_coordinates(self.sc, [self.sqsz * 2, self.sqsz])
        ]
