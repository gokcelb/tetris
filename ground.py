from __future__ import annotations

EMPTY = 0
FULL = 1


class Ground:
    def __init__(self, sqsz: int, screen_dim: list[int]) -> None:
        self.sqsz = sqsz
        self.screen_dim = screen_dim
        self.blocks = self.init_block_coords()

    def get_squares(self) -> list[dict]:
        squares = []
        for row in self.blocks:
            for col in self.blocks[row]:
                if col['status'] == FULL:
                    squares.append(
                        {'coord': [col['value'], row], 'color': col['color']})
        return squares

    def add_square(self, coord: list[int], color: tuple[int]) -> None:
        row = self.blocks[coord[1]]
        for col in row:
            if col['value'] == coord[0]:
                col['status'] = FULL
                col['color'] = color

    def init_block_coords(self) -> None:
        blocks = {}
        for row in range(0, self.screen_dim[1], self.sqsz):
            blocks[row] = []
            for col in range(0, self.screen_dim[0], self.sqsz):
                blocks[row].append(
                    {'value': col, 'status': EMPTY, 'color': None})
        return blocks
