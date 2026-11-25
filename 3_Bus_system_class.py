class BusManagement:
    def __init__(self):
        self.buses = []
        self.passengers = []


# Create object
management = BusManagement()

# Add buses
management.buses.append("Hanif Express")
management.buses.append("Green Line")

# Add passengers
management.passengers.append("Apon")
management.passengers.append("Rahim")


# Display information
print("Buses:", management.buses)
print("Passengers:", management.passengers)