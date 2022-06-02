from __future__ import annotations
import threading
import time
from shape.shape import Shape
from collider import VERTICAL_COLLISION, CollisionDetector


class Gravity(threading.Thread):
    def __init__(self, collider: CollisionDetector):
        threading.Thread.__init__(self)
        self.collider = collider

    def set_shape(self, shape: Shape) -> Gravity:
        self.shape = shape
        return self

    def run(self):
        self.pull()

    def pull(self) -> None:
        while self.collider.collision(self.shape) != VERTICAL_COLLISION:
            for coord in self.shape.curr_coord_list:
                coord[1] += self.shape.sqsz
            self.shape.curr_center[1] += self.shape.sqsz
            time.sleep(0.5)
