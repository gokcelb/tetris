from shape.shape import Shape

HORIZONTAL_COLLISION = 'horizontal'
VERTICAL_COLLISION = 'vertical'
NO_COLLISION = 'none'


class CollisionDetector:
    def __init__(self, screen_dim):
        self.screen_dim = screen_dim
        self.objects: list[Shape] = []

    def collision(self, object: Shape, direction: int = None) -> str:
        squares_on_air = object.curr_coord_list

        for o in self.objects:
            if object is o:
                continue

            squares_on_ground = o.curr_coord_list

            for soa_x, soa_y in squares_on_air:
                for sog_x, sog_y in squares_on_ground:
                    if sog_y - soa_y == 20 and soa_x == sog_x:
                        return VERTICAL_COLLISION

                    if direction and soa_x - sog_x == 20 * direction and soa_y == sog_y:
                        return HORIZONTAL_COLLISION

        return self.is_on_ground(object)

    def is_on_ground(self, object: Shape) -> bool:
        for coord in object.curr_coord_list:
            if self.screen_dim[1] - coord[1] <= object.sqsz:
                return VERTICAL_COLLISION
        return NO_COLLISION

    def add_object(self, object) -> None:
        self.objects.append(object)
