import math 

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override this method.")
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
class Cicle(Shape):
    def __init__(self,raduis):
        self.raduis = raduis

    def area(self):
        return self.raduis*self.raduis*math.pi