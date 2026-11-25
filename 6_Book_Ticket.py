
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


class BusManagement:
    def __init__(self):
        self.buses = []
        self.passengers = []

    def add_bus(self, number, route, seats):
        new_bus = Bus(number, route, seats)
        self.buses.append(new_bus)
        print("Bus Added Successfully!")

    def book_ticket(self, bus_number, name, phone):

        # Find bus
        for bus in self.buses:

            if bus.number == bus_number:

                # Check seat availability
                if bus.seats > 0:

                    # Create passenger
                    passenger = Passenger(name, phone, bus)

                    # Add passenger
                    self.passengers.append(passenger)

                    # Reduce available seat
                    bus.seats -= 1

                    print("Ticket Booked Successfully!")
                    print("Passenger:", name)
                    print("Phone:", phone)
                    print("Bus:", bus.number)
                    print("Route:", bus.route)
                    print("Available Seats:", bus.seats)

                    return

                else:
                    print("Sorry! No Seats Available.")
                    return

        print("Bus Not Found!")


# Create system
system = BusManagement()

# Add buses
system.add_bus("101", "Dhaka to Jessore", 2)
system.add_bus("102", "Dhaka to Khulna", 3)

# Book ticket
system.book_ticket("101", "Apon", "01712345678")

# Book another ticket
system.book_ticket("101", "Rahim", "01812345678")

# Try booking when full
system.book_ticket("101", "Karim", "01912345678")
