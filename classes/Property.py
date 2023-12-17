class Property:
    def __init__(self, area: int, rooms: int, price: int, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        final_string = f"Area: {self.area}, Rooms: {self.rooms}, Price: {self.price}, Address: {self.address}"
        return final_string
