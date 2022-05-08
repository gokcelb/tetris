from __future__ import annotations
import threading


class Gravity(threading.Thread):
    def __init__(self, screen_height):
        threading.Thread.__init__(self)
        self.shape = None
        self.force = 8
        self.screen_height = screen_height

    def set_shape(self, shape) -> Gravity:
        self.shape = shape
        return self

    def run(self):
        print('Starting ' + self.name)
        self.shape.fall(self.screen_height, self.force)
        print('Exiting ' + self.name)
