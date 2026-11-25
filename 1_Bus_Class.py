class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            print("Seat booked successfully!")
        else:
            print("Sorry! No seats available.")


# Create a bus object
bus1 = Bus(101, "Dhaka to Jessore", 40)

# Display information
print("Bus Number:", bus1.number)
print("Route:", bus1.route)
print("Total Seats:", bus1.total_seats)
print("Available Seats:", bus1.available_seats())

# Book seats
bus1.book_seat()
bus1.book_seat()

# Check available seats again
print("Available Seats:", bus1.available_seats())