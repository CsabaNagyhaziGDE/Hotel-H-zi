from room import Room

class SingleRoom(Room):
    def __init__(self, number, price, comfort_level):
        super().__init__(number, price)
        self.extras.append("single bed")

    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
            return f"A(z) {self.number} szoba sikeresen lefoglalva."
        else:
            return "A szoba már foglalt."

    def unbook_room(self):
        if self.is_booked:
            self.is_booked = False
            return f"A(z) {self.number} szoba foglalása sikeresen törölve."
        else:
            return "A szoba nem volt foglalt."

    def __str__(self):
        return f"{self.number}"