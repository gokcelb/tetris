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
            self.rotate(self.curr_coord_list)
        return self.curr_coord_list

    @abstractmethod
    def init_coordinates(self):
        raise NotImplementedError

    @abstractmethod
    def rotate(self, old_coord_list):
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

    def rotate(self, old_coord_list):
        ref_coord = old_coord_list[0]
        ref_x = ref_coord[0]
        ref_y = ref_coord[1]
        rotated_coord_list = [ref_coord]

        for i in range(1, len(old_coord_list)):
            x = old_coord_list[i][0]
            y = old_coord_list[i][1]

            zone_90 = x > ref_x and y == ref_y
            zone_180 = x == ref_x and y > ref_y
            zone_270 = x < ref_x and y == ref_y
            zone_360 = x == ref_x and y < ref_y

            if zone_90:
                new_coord = [ref_x, ref_y + (x - ref_x)]
            elif zone_180:
                new_coord = [ref_x - (y - ref_y), ref_y]
            elif zone_270:
                new_coord = [ref_x, ref_y - (ref_x - x)]
            elif zone_360:
                new_coord = [ref_x + (ref_y - y), ref_y]
            rotated_coord_list.append(new_coord)

        self.curr_coord_list = rotated_coord_list
        return self.curr_coord_list

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

    def rotate(self, old_coord_list):
        ref_coord = old_coord_list[0]
        ref_x = ref_coord[0]
        ref_y = ref_coord[1]
        rotated_coord_list = [ref_coord]

        for i in range(1, len(old_coord_list)):
            x = old_coord_list[i][0]
            y = old_coord_list[i][1]

            zone_90 = x > ref_x and y >= ref_y
            zone_180 = x <= ref_x and y > ref_y
            zone_270 = x < ref_x and y <= ref_y
            zone_360 = x >= ref_x and y < ref_y

            if zone_90:
                if y == ref_y:
                    new_coord = [ref_x, ref_y + (x - ref_x)]
                elif y > ref_y:
                    new_coord = [ref_x - (y - ref_y), ref_y + (x - ref_x)]
            elif zone_180:
                if x == ref_x:
                    new_coord = [ref_x - (y - ref_y), ref_y]
                elif x < ref_x:
                    new_coord = [ref_x - (y - ref_y), ref_y - (ref_x - x)]
            elif zone_270:
                if y == ref_y:
                    new_coord = [ref_x, ref_y - (ref_x - x)]
                elif y < ref_y:
                    new_coord = [ref_x + (ref_y - y), ref_y - (ref_x - x)]
            elif zone_360:
                if x == ref_x:
                    new_coord = [ref_x + (ref_y - y), ref_y]
                elif x > ref_x:
                    new_coord = [ref_x + (ref_y - y), ref_y + (x - ref_x)]
            rotated_coord_list.append(new_coord)

        self.curr_coord_list = rotated_coord_list
        return self.curr_coord_list

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

    def rotate(self, old_coord_list):
        ref_coord = old_coord_list[0]
        ref_x = ref_coord[0]
        ref_y = ref_coord[1]
        odd_x = old_coord_list[3][0]
        odd_y = old_coord_list[3][1]
        rotated_coord_list = [ref_coord]

        zone_90 = odd_x == ref_x and odd_y > ref_y
        zone_180 = odd_x < ref_x and odd_y == ref_y
        zone_270 = odd_x == ref_x and odd_y < ref_y
        zone_360 = odd_x > ref_x and odd_y == ref_y

        for i in range(1, len(old_coord_list)):
            x = old_coord_list[i][0]
            y = old_coord_list[i][1]

            if zone_90:
                if y == ref_y:
                    new_coord = [ref_x, ref_y + (x - ref_x)]
                elif y > ref_y:
                    new_coord = [ref_x - (y - ref_y), ref_y + (x - ref_x)]
            elif zone_180:
                if x == ref_x:
                    new_coord = [ref_x - (y - ref_y), ref_y]
                elif x < ref_x:
                    new_coord = [ref_x - (y - ref_y), ref_y - (ref_x - x)]
            elif zone_270:
                if y == ref_y:
                    new_coord = [ref_x, ref_y - (ref_x - x)]
                elif y < ref_y:
                    new_coord = [ref_x + (ref_y - y), ref_y - (ref_x - x)]
            elif zone_360:
                if x == ref_x:
                    new_coord = [ref_x + (ref_y - y), ref_y]
                elif x > ref_x:
                    new_coord = [ref_x + (ref_y - y), ref_y + (x - ref_x)]
            rotated_coord_list.append(new_coord)

        self.curr_coord_list = rotated_coord_list
        return self.curr_coord_list

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

    def rotate(self, old_coord_list):
        ref_coord = old_coord_list[0]
        ref_x = ref_coord[0]
        ref_y = ref_coord[1]
        rotated_coord_list = [ref_coord]

        for i in range(1, len(old_coord_list)):
            x = old_coord_list[i][0]
            y = old_coord_list[i][1]

            zone_90 = x > ref_x and y >= ref_y
            zone_180 = x <= ref_x and y > ref_y
            zone_270 = x < ref_x and y <= ref_y
            zone_360 = x >= ref_x and y < ref_y

            if zone_90:
                if y == ref_y:
                    new_coord = [ref_x, ref_y + (x - ref_x)]
                elif y > ref_y:
                    new_coord = [ref_x - (y - ref_y), ref_y + (x - ref_x)]
            elif zone_180:
                if x == ref_x:
                    new_coord = [ref_x - (y - ref_y), ref_y]
                elif x < ref_x:
                    new_coord = [ref_x - (y - ref_y), ref_y - (ref_x - x)]
            elif zone_270:
                if y == ref_y:
                    new_coord = [ref_x, ref_y - (ref_x - x)]
                elif y < ref_y:
                    new_coord = [ref_x + (ref_y - y), ref_y - (ref_x - x)]
            elif zone_360:
                if x == ref_x:
                    new_coord = [ref_x + (ref_y - y), ref_y]
                elif x > ref_x:
                    new_coord = [ref_x + (ref_y - y), ref_y + (x - ref_x)]
            rotated_coord_list.append(new_coord)

        self.curr_coord_list = rotated_coord_list
        return self.curr_coord_list

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

    def rotate(self, old_coord_list):
        ref_coord = old_coord_list[0]
        ref_x = ref_coord[0]
        ref_y = ref_coord[1]
        rotated_coord_list = [ref_coord]

        for i in range(1, len(old_coord_list)):
            x = old_coord_list[i][0]
            y = old_coord_list[i][1]

            zone_90 = x > ref_x and y >= ref_y
            zone_180 = x <= ref_x and y > ref_y
            zone_270 = x < ref_x and y <= ref_y
            zone_360 = x >= ref_x and y < ref_y

            if zone_90:
                if y == ref_y:
                    new_coord = [ref_x, ref_y + (x - ref_x)]
                elif y > ref_y:
                    new_coord = [ref_x - (y - ref_y), ref_y + (x - ref_x)]
            elif zone_180:
                if x == ref_x:
                    new_coord = [ref_x - (y - ref_y), ref_y]
                elif x < ref_x:
                    new_coord = [ref_x - (y - ref_y), ref_y - (ref_x - x)]
            elif zone_270:
                if y == ref_y:
                    new_coord = [ref_x, ref_y - (ref_x - x)]
                elif y < ref_y:
                    new_coord = [ref_x + (ref_y - y), ref_y - (ref_x - x)]
            elif zone_360:
                if x == ref_x:
                    new_coord = [ref_x + (ref_y - y), ref_y]
                elif x > ref_x:
                    new_coord = [ref_x + (ref_y - y), ref_y + (x - ref_x)]
            rotated_coord_list.append(new_coord)

        self.curr_coord_list = rotated_coord_list
        return self.curr_coord_list
