class Rectangle(object):
    def __init__(self, width, height, pi):
        self.width = width
        self.height = height
        self.pi = pi 
       
        
    def area(self):
        print(f'AREA: {self.width}x{self.height}x{self.pi}')
        return self.width * self.height * self.pi 
    
class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width,width)
        
class Ellipse(Rectangle):
    def __init__(self, major_axis, minor_axis, pi):
        self.major_axis = major_axis
        self.minor_axis = minor_axis
        super().__init__( major_axis, minor_axis, pi)
        
        
class Circle(Rectangle):
    def __init__(self, radius, pi):
        self.radius = radius
        super().__init__( radius, radius, pi)

