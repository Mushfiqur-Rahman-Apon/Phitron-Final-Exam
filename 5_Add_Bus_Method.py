class Bus:
    def __init__(self, number, route, seats):
        self.number = number
        self.route = route
        self.seats = seats


class BusManagement:
    def __init__(self):
        self.buses = []
        self.admin_logged_in = False

    def add_bus(self, number, route, seats):
        if self.admin_logged_in:
            new_bus = Bus(number, route, seats)

            self.buses.append(new_bus)

            print("Bus Added Successfully!")

        else:
            print("Only Admin Can Add Bus!")


# Create object
system = BusManagement()

# Try without admin login
system.add_bus("Dhaka-101", "Dhaka to Jessore", 40)

# Admin login
system.admin_logged_in = True

# Add bus
system.add_bus("Dhaka-102", "Dhaka to Khulna", 50)

# Display buses
for bus in system.buses:
    print(bus.number, bus.route, bus.seats)