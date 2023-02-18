class Attendee:

    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def displayAttendee(self):
        print("name : {}, Tickets {}".format(self.name, self.tickets))

    def addTickets(self):
        self.tickets += 1
        print("{} tickets inscreased to {}".format(self.name, self.tickets))


attende1 = Attendee("javier Chavez", 1)
