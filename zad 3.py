class Property:
    def __init__(self, area: int, rooms: int, price: int, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        final_string = f"Area: {self.area}, Rooms: {self.rooms}, Price: {self.price}, Address: {self.address}"
        return final_string


class House(Property):
    def __init__(self, area: int, rooms: int, price: int, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        final_string = f"{self.__class__.__name__}: {super().__str__()}, Plot: {self.plot}"
        return final_string


class Flat(Property):
    def __init__(self, area: int, rooms: int, price: int, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        final_string = f"{self.__class__.__name__}: {super().__str__()}, Floor: {self.floor}"
        return final_string


house1 = House(area=150, rooms=4, price=300000, address="ul. Bogucika 1", plot=500)
flat1 = Flat(area=80, rooms=2, price=150000, address="ul. Jana Matejki 2", floor=2)

print(house1)
print(flat1)
