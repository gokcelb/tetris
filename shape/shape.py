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
        print('coordinates method running')
        rotations = [0, 90, 180, 270]
        rotation_degree = rotations[random.randint(0, len(rotations) - 1)]
        if rotation_degree == 0:
            print('rotation degree is 0')
            return self.init_coordinates()

        return self.rotate(90)

    def rotate(self, rotation_degree):
        init_coord = self.init_coordinates()
        origin = init_coord[0]
        rotated_coordinates_list = [origin]

        if rotation_degree == 90:
            print('Rotating 90 degrees...')
            for i, coordinates in enumerate(init_coord):
                if i == 0:
                    continue

                x = coordinates[0]
                y = coordinates[1]
                origin_x = origin[0]
                origin_y = origin[1]
                if y == origin_y:
                    new_coord = [origin_x, origin_y + (x - origin_x)]
                elif y - origin_y == self.sqsz:
                    new_coord = [origin_x - (y - origin_y), origin_y + (x - origin_x)]
                rotated_coordinates_list.append(new_coord)
            print(rotated_coordinates_list)
            return rotated_coordinates_list

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

