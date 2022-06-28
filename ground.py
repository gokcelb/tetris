from __future__ import annotations

# Block status
EMPTY = 0
FULL = 1

# Square status
INTACT = 'intact'
FRAGMENTED = 'fragmented'
NA = 'na'


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
                col['square_status'] = INTACT

    def init_block_coords(self) -> None:
        blocks = {}
        for row in range(0, self.screen_dim[1], self.sqsz):
            blocks[row] = []
            for col in range(0, self.screen_dim[0], self.sqsz):
                blocks[row].append(
                    {'value': col, 'status': EMPTY, 'color': None, 'square_status': NA})
        return blocks

    def destroy_complete_rows(self) -> None:
        for row in self.blocks:
            if self.__row_is_complete(self.blocks[row]):
                self.__destroy_row(self.blocks[row])

    def rearrange_squares(self) -> None:
        for row in self.blocks:
            next_row = row + self.sqsz
            if next_row == self.screen_dim[1]:
                continue

            for col in self.blocks[row]:
                next_cols = self.__find_next_empty_cols(col, next_row)
                if next_cols is None:
                    continue

                for next_col in next_cols:
                    self.__move_col_down(col, next_col)

    def __find_next_empty_cols(self, col, next_row) -> list[dict]:
        next_cols = []
        while next_row + self.sqsz <= self.screen_dim[1]:
            for next_col in self.blocks[next_row]:
                if next_col['status'] == EMPTY and next_col['value'] == col['value']:
                    next_cols.append(next_col)
            next_row += self.sqsz
        return next_cols

    def __move_col_down(self, col, next_col) -> None:
        temp = col.copy()
        col['status'] = EMPTY
        col['color'] = None
        col['square_status'] = INTACT
        next_col['status'] = temp['status']
        next_col['color'] = temp['color']
        next_col['square_status'] = temp['square_status']

    def __row_is_complete(self, row) -> bool:
        for col in row:
            if col['status'] != FULL:
                return False
        return True

    def __destroy_row(self, row) -> None:
        for col in row:
            col['status'] = EMPTY
            col['square_status'] = FRAGMENTED
