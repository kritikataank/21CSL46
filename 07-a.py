import math

class Shape:
    def __init__(self):
        self.area =0
        self.name=""
    def showarea(self):
        print("The area of ", self.name, " is ", self.area, " units.")

class Circle(Shape):
    def __init__(self, radius):
        self.area=0
        self.name="circle"
        self.radius = radius

    def calcarea(self):
        self.area = (self.radius**2)*math.pi

class Rectangle(Shape):
    def __init__(self, breadth, length):
        self.area = 0
        self.name ="rectangle"
        self.breadth = breadth
        self.length = length
    def calcarea(self):
        self.area=self.length*self.breadth

class Triangle(Shape):
    def __init__(self, base, height):
        self.area = 0
        self.name ="tringle"
        self.height = height
        self.base = base
    def calcarea(self):
        self.area = 0.5*self.base*self.height


c1=Circle(5)
c1.calcarea()
c1.showarea()

r1=Rectangle(5,4)
r1.calcarea()
r1.showarea()

t1=Triangle(3,4)
t1.calcarea()
t1.showarea()