import abc

# TASK 1
def print_divider(decorated_func):
    """Print a divider before and after a method is called"""
    def method_wrapper(self, *args, **kwargs):
        print("-" * 40)
        decorated_func(self, *args, **kwargs)
        print("-" * 40)

    return method_wrapper


class Shape(metaclass=abc.ABCMeta):
    """Define Shape class"""

    @abc.abstractmethod
    def calc_perimeter(self):
        """Method documentation"""
        return


class Triangle(Shape):
    """Define Triangle class"""
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @print_divider
    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented!", perim)
        return perim


class Rectangle(Shape):
    """Define Rectangle class"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @print_divider
    def calc_perimeter(self):
        """Implement calc_perimeter method"""
        perim = 2 * (self.a + self.b)
        print("Consider me implemented!", perim)
        return perim


class Square(Rectangle):
    """Define Square class"""

    def __init__(self, a):
        self.a = a
        self.b = a

# Instantiate classes
triangle = Triangle(2, 5, 3)
rectangle = Rectangle(2, 4)
square = Square(7)

# Call methods
triangle.calc_perimeter()
rectangle.calc_perimeter()
square.calc_perimeter()
