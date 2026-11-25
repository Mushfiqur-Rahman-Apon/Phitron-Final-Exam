
class Bus:
    def __init__(self, number, route, seats):
        self.number = number
        self.route = route
        self.seats = seats


class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus
        self.fare = 500


class BusManagement:
    def __init__(self):
        self.buses = []
        self.passengers = []

    def add_bus(self, number, route, seats):
        bus = Bus(number, route, seats)
        self.buses.append(bus)

    def book_ticket(self, bus_number, name, phone):

        for bus in self.buses:

            if bus.number == bus_number:

                if bus.seats > 0:

                    passenger = Passenger(name, phone, bus)

                    self.passengers.append(passenger)

                    bus.seats -= 1

                    print("\n===== TICKET BOOKED =====")
                    print("Passenger Name:", passenger.name)
                    print("Phone:", passenger.phone)
                    print("Bus Number:", bus.number)
                    print("Route:", bus.route)
                    print("Ticket Fare: ৳", passenger.fare)
                    print("Available Seats:", bus.seats)

                    return

                else:
                    print("No Seats Available!")
                    return

        print("Bus Not Found!")


# Create System
system = BusManagement()

# Add Bus
system.add_bus("101", "Dhaka to Jessore", 40)

# Book Ticket
system.book_ticket("101", "Apon", "01712345678")
