from classes.Property import Property


class Flat(Property):
    def __init__(
        self, area: int, rooms: int, price: int, address: str, floor: int
    ):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        final_string = f"{self.__class__.__name__}: {super().__str__()}, Floor: {self.floor}"
        return final_string
