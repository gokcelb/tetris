from __future__ import annotations
from shape.shape import Shape

HORIZONTAL_COLLISION = 'horizontal'
VERTICAL_COLLISION = 'vertical'
NO_COLLISION = 'none'


class CollisionDetector:
    def __init__(self, screen_dim):
        self.screen_dim = screen_dim
        self.squares_on_ground: list[list[int]] = []

    def collision(self, shape: Shape, direction: int = None) -> str:
        squares_on_air = shape.curr_coord_list

        for soa_x, soa_y in squares_on_air:
            for sog_x, sog_y in self.squares_on_ground:
                if sog_y - soa_y == 20 and soa_x == sog_x:
                    return VERTICAL_COLLISION

                if direction and soa_x - sog_x == 20 * direction and soa_y == sog_y:
                    return HORIZONTAL_COLLISION

        return self.is_on_ground(shape)

    def is_on_ground(self, shape: Shape) -> bool:
        for coord in shape.curr_coord_list:
            if self.screen_dim[1] - coord[1] <= shape.sqsz:
                return VERTICAL_COLLISION
        return NO_COLLISION

    def set_square_coords(self, square_coords: list[list[int]]) -> None:
        self.squares_on_ground = square_coords
