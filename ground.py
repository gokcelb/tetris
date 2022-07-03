from __future__ import annotations

EMPTY = 'empty'
FULL = 'full'

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
                    {
                        'value': col,
                        'status': EMPTY,
                        'color': None,
                    }
                )
        return blocks

    def destroy_complete_rows(self) -> None:
        num_of_rows_destroyed = 0
        for row in self.blocks:
            if self.__row_is_complete(self.blocks[row]):
                self.__destroy_row(self.blocks[row])
                num_of_rows_destroyed += 1

        if num_of_rows_destroyed > 0:
            self.rearrange_squares(num_of_rows_destroyed)

    def rearrange_squares(self, num_of_rows_destroyed: int) -> None:
        curr_row = self.screen_dim[1] - self.sqsz
        while curr_row > 0:
            for col in self.blocks[curr_row]:
                if curr_row + (self.sqsz + num_of_rows_destroyed) >= self.screen_dim[1]:
                    continue

                if col['status'] == FULL:
                    self.__move_col_down(num_of_rows_destroyed, col, curr_row)

            curr_row -= self.sqsz

    def __move_col_down(self, by, col, row):
        target_row = row + (self.sqsz * by)
        target_col = self.__find_target_col(col, target_row)

        target_col['status'] = col['status']
        target_col['color'] = col['color']
        col['status'] = EMPTY
        col['color'] = None

    def __find_target_col(self, curr_col, target_row) -> dict:
        for col in self.blocks[target_row]:
            if col['value'] == curr_col['value']:
                return col

    def __row_is_complete(self, row) -> bool:
        for col in row:
            if col['status'] == EMPTY:
                return False
        return True

    def __destroy_row(self, row) -> None:
        for col in row:
            col['status'] = EMPTY
