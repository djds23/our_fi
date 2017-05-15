import math

def distance(point_one, point_two):
    return math.sqrt(
        ((point_one[0] - point_two[0])**2) +
        ((point_one[1] - point_two[1])**2)
    )

class Direction(object):
    def __init__(self, is_left, is_up):
        self.is_left = is_left
        self.is_up = is_up


