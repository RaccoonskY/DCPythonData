"""
Demonstration of OOP in Python
This module must not be used in any practical way
but reminding how to write OOP in Python
"""
class Planet:

    __private_value = 0
# class constructor
    def __init__(self, name):
        self.name = name

# redifine how object becomes int
    def __int__(self):
        return self.__private_value
# redefine how object is printed
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


pl = Planet("Name")


print(int(pl))