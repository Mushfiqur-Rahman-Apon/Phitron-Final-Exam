class Bus:
    def __init__(self, bus_name):
        self.bus_name = bus_name


class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus


# Create Bus object
bus1 = Bus("Hanif Express")

# Create Passenger object
p1 = Passenger("Apon", "01712345678", bus1)

# Print information
print("Name:", p1.name)
print("Phone:", p1.phone)
print("Bus:", p1.bus.bus_name)