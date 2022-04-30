import random

class ShapeGenerator:
    def __init__(self, square_size):
        self.sqsz = square_size

    def coordinates(self):
        coordinates_list = [
            [[0, 0], [self.sqsz, 0], [self.sqsz*2, 0], [self.sqsz*3, 0]],
            [[0, 0], [self.sqsz, 0], [self.sqsz*2, 0], [self.sqsz, self.sqsz]],
            [[0, 0], [self.sqsz, 0], [self.sqsz*2, 0], [0, self.sqsz]],
            [[0, 0], [self.sqsz, 0], [self.sqsz*2, 0], [self.sqsz*2, self.sqsz]],
            [[0, 0], [self.sqsz, 0], [self.sqsz, self.sqsz], [self.sqsz*2, self.sqsz]]
        ]
        return coordinates_list[random.randint(0, len(coordinates_list) - 1)]
