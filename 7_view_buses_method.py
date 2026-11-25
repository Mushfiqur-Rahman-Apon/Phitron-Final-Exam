
class Bus:
    def __init__(self, number, route, seats):
        self.number = number
        self.route = route
        self.seats = seats


class BusManagement:
    def __init__(self):
        self.buses = []

    # Add Bus
    def add_bus(self, number, route, seats):
        bus = Bus(number, route, seats)
        self.buses.append(bus)
        print("Bus Added Successfully!")

    # View All Buses
    def show_buses(self):
        if len(self.buses) == 0:
            print("No Buses Available!")
            return

        print("\n========== BUS LIST ==========")

        for bus in self.buses:
            print("Bus Number:", bus.number)
            print("Route:", bus.route)
            print("Available Seats:", bus.seats)
            print("-----------------------------")


# Create Bus Management Object
system = BusManagement()

# Add Buses
system.add_bus("101", "Dhaka to Jessore", 40)
system.add_bus("102", "Dhaka to Khulna", 35)
system.add_bus("103", "Dhaka to Chittagong", 50)

# Display All Buses
system.show_buses()
