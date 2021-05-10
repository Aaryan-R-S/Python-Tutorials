from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printArea(this):
        return 0 

# Important No object can be created directly from Shape class(abstract class)
# e.g.   y = Shape()  X not possible

class Rectangle(Shape):
    type = 'Rectangle'
    sides = 4

    def __init__(this):
        this.length = 7
        this.breadth = 8

# Without printarea func it will show error as its made compulsory at Shape
    def printArea(this):
        return this.length * this.breadth

rect1 = Rectangle()
print(rect1.printArea())