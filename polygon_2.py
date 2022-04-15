from abc import ABC, abstractmethod

class GeometryShape(ABC):
    """Абстрактный класс ФИГУРА"""
    def __init__(self, sides, *args):
        self.sides = sides

    @abstractmethod
    def perimetr(self):
        return ''

    @abstractmethod
    def area(self):
        return ''

    @abstractmethod
    def num_of_angles(self):
        return ''

    @abstractmethod
    def sum_of_angles(self):
        return ''

class StraightTriangle(GeometryShape):

    def __init__(self, sides, *args):
        super().__init__(sides, *args)
        self.sides = 3
        self.length = (5, 7)

    def perimetr(self):
        return (self.length[0] + self.length[1]) ** 0.5 + self.length[0] + self.length[1]

    def area(self):
        return self.length[0] * self.length[1] * 0.5

    def num_of_angles(self):
        return self.sides

    def sum_of_angles(self):
        return (self.sides - 2) * 180


class Square(GeometryShape):

    def __init__(self, sides, *args):
        super().__init__(sides, *args)
        self.sides = 4
        self.length = 5

    def perimetr(self):
        return self.length * self.sides

    def area(self):
        return self.length ** 2

    def num_of_angles(self):
        return self.sides

    def sum_of_angles(self):
        return (self.sides - 2) * 180