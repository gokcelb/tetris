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
            return self.init_coordinates()

        return self.__rotate(rotation_degree)

    def __rotate(self, rotation_degree):
        init_coord_list = self.init_coordinates()
        ref_coord = init_coord_list[0]
        rotated_coordinates_list = [ref_coord]

        for i, coord in enumerate(init_coord_list):
            if i == 0:
                continue

            if rotation_degree == 90:
                new_coord = self.rotate_ninety(coord, ref_coord)
            elif rotation_degree == 180:
                new_coord = self.rotate_one_hundred_eighty(coord, ref_coord)
            elif rotation_degree == 270:
                new_coord = self.rotate_two_hundred_seventy(coord, ref_coord)
            rotated_coordinates_list.append(new_coord)

        return rotated_coordinates_list

    def rotate_ninety(self, coord, ref_coord):
        x = coord[0]
        y = coord[1]
        # reference coordinates are the coordinates of
        # the square whose coordinates will remain stable
        ref_x = ref_coord[0]
        ref_y = ref_coord[1]

        if x - ref_x >= 0 and y - ref_y >= 0 and y == ref_y:
            return [ref_x, ref_y + (x - ref_x)]
        elif x - ref_x >= 0 and y - ref_y >= 0 and y - ref_y == self.sqsz:
            return [ref_x - (y - ref_y), ref_y + (x - ref_x)]

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

        return rotated_coord_list

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

        return rotated_coord_list

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

        return rotated_coord_list

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

        return rotated_coord_list

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

        return rotated_coord_list
