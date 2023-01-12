"""
Little example of inheritance in Python
Pet (super object) -> Dog

isinstance(A, B) - checks if A is an instance of B
issubclass(A, B) - checks if A is a subclass of B

"""

class Pet:
    def __init__(self, name=None):
        self.name = name


class Dog(Pet, M1):
    def __init__(self, name, breed=None):
        super(Dog, self).__init__(name)
        #super(Pet,self).__init__(name)
        self.breed = breed
        self.__private = name+" is private" #it's private data
        #but we can access private data with _Dog__breed

    def voice(self):
        return "{0}: waw".format(self.name)


new_dog = Dog("Balloon","default")

print(new_dog.name)
