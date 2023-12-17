class Library:
    def __init__(
        self,
        name: str,
        city: str,
        street: str,
        zip_code: str,
        open_hours: str,
        phone: str,
    ):
        self.name = name
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Library: {self.name}\nCity: {self.city}\nStreet: {self.street}\nZip code: {self.zip_code}\n"
            f"Open hours: {self.open_hours}\nPhone: {self.phone}\n"
        )
