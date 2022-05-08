from shape.shape import Shape


class Ground:
    def __init__(self) -> None:
        self.shapes: list[Shape] = []

    def add_shape(self, shape: Shape) -> None:
        self.shapes.append(shape)
