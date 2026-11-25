
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

    # Add Bus
    def add_bus(self, number, route, seats):

        if not number or not route:
            print("Error: Bus number and route are required!")
            return

        if not isinstance(seats, int) or seats <= 0:
            print("Error: Seats must be a positive number!")
            return

        for bus in self.buses:
            if bus.number == number:
                print("Error: Bus already exists!")
                return

        bus = Bus(number, route, seats)
        self.buses.append(bus)

        print("Bus Added Successfully!")

    # View Buses
    def show_buses(self):

        if not self.buses:
            print("Sorry! No Buses Available.")
            return

        print("\n===== BUS LIST =====")

        for bus in self.buses:
            print("Bus Number:", bus.number)
            print("Route:", bus.route)
            print("Available Seats:", bus.seats)
            print("-------------------")

    # Book Ticket
    def book_ticket(self, bus_number, name, phone):

        if not bus_number or not name or not phone:
            print("Error: All fields are required!")
            return

        if not phone.isdigit() or len(phone) != 11:
            print("Error: Enter a valid 11-digit phone number!")
            return

        for bus in self.buses:

            if bus.number == bus_number:

                if bus.seats > 0:

                    passenger = Passenger(name, phone, bus)

                    self.passengers.append(passenger)

                    bus.seats -= 1

                    print("\nTicket Booked Successfully!")
                    print("Passenger:", name)
                    print("Phone:", phone)
                    print("Bus:", bus.number)
                    print("Fare: ৳", passenger.fare)
                    print("Remaining Seats:", bus.seats)

                    return

                else:
                    print("Sorry! No Seats Available.")
                    return

        print("Error: Bus Not Found!")


# Create System
system = BusManagement()

# Sample Bus
system.add_bus("101", "Dhaka to Jessore", 40)


# Main User Menu
while True:

    print("\n======= USER MENU =======")
    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. View Buses")
    print("4. Exit")

    choice = input("Enter Your Choice (1-4): ").strip()

    if choice == "1":

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username == "admin" and password == "1234":

            print("Admin Login Successful!")

            while True:

                print("\n======= ADMIN MENU =======")
                print("1. Add Bus")
                print("2. View All Buses")
                print("3. Logout")

                admin_choice = input("Enter Choice (1-3): ").strip()

                if admin_choice == "1":

                    number = input("Enter Bus Number: ").strip()
                    route = input("Enter Route: ").strip()

                    try:
                        seats = int(input("Enter Total Seats: "))
                        system.add_bus(number, route, seats)

                    except ValueError:
                        print("Error: Please enter a valid number!")

                elif admin_choice == "2":
                    system.show_buses()

                elif admin_choice == "3":
                    print("Admin Logged Out Successfully!")
                    break

                else:
                    print("Invalid Admin Choice! Please select 1-3.")

        else:
            print("Login Failed! Invalid Username or Password.")

    elif choice == "2":

        system.show_buses()

        bus_number = input("Enter Bus Number: ").strip()
        name = input("Enter Passenger Name: ").strip()
        phone = input("Enter Phone Number: ").strip()

        system.book_ticket(bus_number, name, phone)

    elif choice == "3":
        system.show_buses()

    elif choice == "4":
        print("Thank You! Have a Safe Journey.")
        break

    else:
        print("Invalid Choice! Please select between 1 and 4.")
