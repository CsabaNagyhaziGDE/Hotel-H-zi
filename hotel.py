from datetime import datetime

class Hotel:
    def __init__(self, name):
        self.name = name
        self.room = []
        self.bookings = []

    def add_room(self, room):
        self.room.append(room)

    def check_availability(self):
        available_room = [room.number for room in self.room if not room.is_booked]
        for room in self.room:
            if not room.is_booked:
                available_room.append(room.number)
        return available_room

    def book_room_by_number(self, number, date):
        for room in self.room:
            if room.number == number and not room.is_booked:
                room.is_booked = True
                booking = Booking(number, date)
                self.bookings.append(booking)
                return f"A {number} szoba sikeresen lefoglalva."
            return "A megadott szobaszám nem található vagy már foglalt."



    def get_room_prices(self):
        return {room.number: room.price for room in self.room}

    def book_room_by_date(self, number, date):
        for room in self.room:
            if room.number == number:
                if not room.is_booked:
                    room.is_booked = True
                    return f"A {room.number} szoba {date} dátumra sikeresen lefoglalva. Ár: {room.price}"
                else:
                    return "A szoba már foglalt."
        return "A megadott szobaszám nem található."

    def get_price_by_date(self, number, date):
        for room in self.rooms:
            if room.number == number:
                for booking in self.bookings:
                    if booking.room_number == number and booking.date == date:
                        return room.price
                return "A megadott dátumra a szoba nincs foglalva."
        return "A megadott szobaszám nem található."


    def cancel_booking(self, number):
        for booking in self.bookings:
            if booking.room.number == number:
                booking.room.is_booked = False
                self.bookings.remove(booking)
                return f"A {number} szoba foglalása sikeresen törölve."
        return "A megadott szobaszámhoz nincs foglalás."
        for room in self.room:
            if room.number == number:
                for booking in self.bookings:
                    if booking.room_number == number:
                        self.bookings.remove(booking)
                        room.is_booked = False
                        return f"A(z) {number} szoba foglalása sikeresen törölve."
                return "A megadott szobaszámra nincs foglalás."
        return "A megadott szobaszám nem található."
