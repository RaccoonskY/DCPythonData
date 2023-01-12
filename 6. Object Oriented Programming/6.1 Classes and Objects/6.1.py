

class House:
    """
    class describes house with
    number of floors(floors),color(color)
    and has_balcony(True\False)
    """
    def __init__(self, floors=int(), color=str(), has_balcony=bool()):
        self.floors = floors
        self.color = color
        self.has_balcony = has_balcony

    """
    Prints info of house
    """
    def __str__(self):
        return(
            f"Floors:{self.floors}"
            f"\nColor:{self.color}"
            f"\nWith balcony:{'yes' if self.has_balcony else 'no'}")

    def add_floor(self):
        self.floors += 1


first_h = House(floors=1, color="Red",has_balcony=True)

second_h = House(floors=1, color="Red",has_balcony=True)

third_h = House(floors=1, color="Red",has_balcony=True)

print(first_h)
first_h.add_floor()
print(first_h)