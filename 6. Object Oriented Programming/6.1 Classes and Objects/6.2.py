"""
 На координатной плоскости рисуются окружности,
 у каждой окружности следующие параметры:
 координаты X и Y центра окружности
 и значение R ― это радиус окружности.
 По умолчанию центр находится в (0, 0),
 а радиус равен 1.
"""
import math


class Circle:
    """
    Circle describes mathematical circle with
    x & y coords, radius (r)
    """

    def __init__(self, x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius**2)

    def get_length(self):
        return math.pi * 2 * self.radius

    def get_distance_to(self, circle):
        return math.sqrt((self.x - circle.x)**2+(self.y - circle.y)**2)

    def is_crossing(self, circle):
        return self.get_distance_to(circle) < self.radius+circle.radius


    def __str__(self):
        return f"x:{self.x}\n" \
               f"y:{self.y}\n" \
               f"area:{self.get_area()}\n" \
               f"length:{self.get_length()}"


circle1 = Circle()
circle2 = Circle(0, 1, 5)

print(circle1.is_crossing(circle2))
print(circle2.is_crossing(circle1))
print(circle1)
print(circle2)