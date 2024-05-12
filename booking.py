class Booking:
    def __init__(self, room, date):
        self.room = room
        self.date = date
  
    def get_room(self):
        return self.room

    def get_date(self):
        return self.date