from classes.Property import Property


class House(Property):
    def __init__(self, area: int, rooms: int, price: int, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        final_string = f"{self.__class__.__name__}: {super().__str__()}, Plot: {self.plot}"
        return final_string
