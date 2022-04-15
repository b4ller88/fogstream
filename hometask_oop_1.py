class Fraction:

    def __init__(self, a, b):
        self.a: int = a
        self.b: int = b

    def __eq__(self, other):
        