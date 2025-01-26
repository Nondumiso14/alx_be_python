import math

class Shape:
    def area(self):
        """
        Calculates the area of a shape.
        
        Raises:
        NotImplementedError: Indicates that derived classes need to override this method.
        """
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
         return self.length * self.width

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
         return math.pi * (self.radius ** 2)


