class Vehicle:
    def __init__(self,made_by: str):
        self.__made_by = made_by

    def go(self):
        print("Vehicle goes")

    def stop(self):
        print("Vehicle stops")

    def get_creator(self):
        print(self.__made_by)
        return {self.__made_by}


class Car(Vehicle):
    def __init__(self,made_by: str,speed: int):
        super().__init__(made_by)
        self.speed = speed

    def jump(self):
        print(f"car jumped on speed {self.speed}")


class Truck(Vehicle):
    def __init__(self, made_by: str, occupancy: int = 0):
        super().__init__(made_by)
        self.occupancy = occupancy

    def load(self):
        self.occupancy += 1

    def unload(self):
        self.occupancy -= 1


car = Car("ford", 100)
car.go()
car.stop()
car.jump()

truck = Truck("hyndai")
truck.load()
print(truck.occupancy)
truck.unload()
print(truck.occupancy)
