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
        self.curr_coord_list = self.init_coordinates()

    def __random_color(self):
        return Shape.COLORS[random.randint(0, len(Shape.COLORS) - 1)]

    def coordinates(self):
        times = [0, 1, 2, 3]
        rotation_count = times[random.randint(0, len(times) - 1)]
        if rotation_count == 0:
            return self.curr_coord_list

        for _ in range(rotation_count):
            self.rotate()
        return self.curr_coord_list

    def rotate(self):
        # const_x and const_y are the coordinates of the square
        # that will always remain constant and unchanging
        const_x = self.curr_coord_list[0][0]
        const_y = self.curr_coord_list[0][1]
        rotated_coord_list = [self.curr_coord_list[0]]
        # ref_x and ref_y are coordinates that the method
        # takes as reference to calculate rotation zones
        ref_x = self.curr_coord_list[3][0]
        ref_y = self.curr_coord_list[3][1]

        zone_90 = ref_x > const_x and ref_y >= const_y
        zone_180 = ref_x <= const_x and ref_y > const_y
        zone_270 = ref_x < const_x and ref_y <= const_y
        zone_360 = ref_x >= const_x and ref_y < const_y

        for i in range(1, len(self.curr_coord_list)):
            x = self.curr_coord_list[i][0]
            y = self.curr_coord_list[i][1]

            if zone_90:
                new_coord = [const_x - (y - const_y), const_y + (x - const_x)]
            elif zone_180:
                new_coord = [const_x - (y - const_y), const_y - (const_x - x)]
            elif zone_270:
                new_coord = [const_x + (const_y - y), const_y - (const_x - x)]
            elif zone_360:
                new_coord = [const_x + (const_y - y), const_y + (x - const_x)]
            rotated_coord_list.append(new_coord)

        self.curr_coord_list = rotated_coord_list
        return self.curr_coord_list

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
