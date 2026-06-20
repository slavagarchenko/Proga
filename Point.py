import math
from functools import reduce


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        if isinstance(other, Point):
            return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def distance_to(self, points, index=0):
        result = []
        if index >= len(points):
            return result
        result.append(self.dist(points[index]))
        return self.distance_to(points, index + 1)

    @staticmethod
    def centroid(points):
        if len(points) == 0:
            return None
        total = reduce(lambda p1, p2: Point(p1.x + p2.x, p1.y + p2.y), points)
        return Point(total.x/len(points), total.y/len(points))

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        raise TypeError

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
