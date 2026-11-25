
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


class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"
        self.logged_in = False

    def login(self, username, password):
        if username == self.username and password == self.password:
            self.logged_in = True
            print("Admin Login Successful!")
            return True
        else:
            print("Invalid Username or Password!")
            return False


class BusManagement:
    def __init__(self):
        self.buses = []
        self.passengers = []

    def add_bus(self, number, route, seats):
        bus = Bus(number, route, seats)
        self.buses.append(bus)
        print("Bus Added Successfully!")

    def show_buses(self):
        if not self.buses:
            print("No Buses Available!")
            return

        print("\n===== AVAILABLE BUSES =====")

        for bus in self.buses:
            print("Bus Number:", bus.number)
            print("Route:", bus.route)
            print("Available Seats:", bus.seats)
            print("-------------------------")

    def book_ticket(self, bus_number, name, phone):
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
                    print("Available Seats:", bus.seats)
                    return

                else:
                    print("No Seats Available!")
                    return

        print("Bus Not Found!")


# Create Objects
admin = Admin()
system = BusManagement()

# Add Sample Buses
system.add_bus("101", "Dhaka to Jessore", 40)
system.add_bus("102", "Dhaka to Khulna", 35)


# USER MENU
while True:

    print("\n========== USER MENU ==========")
    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. View Buses")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    # Admin Login
    if choice == "1":
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if admin.login(username, password):

            while admin.logged_in:
                print("\n===== ADMIN MENU =====")
                print("1. Add Bus")
                print("2. View Buses")
                print("3. Logout")

                admin_choice = input("Enter Choice: ")

                if admin_choice == "1":
                    number = input("Enter Bus Number: ")
                    route = input("Enter Route: ")
                    seats = int(input("Enter Seats: "))

                    system.add_bus(number, route, seats)

                elif admin_choice == "2":
                    system.show_buses()

                elif admin_choice == "3":
                    admin.logged_in = False
                    print("Admin Logged Out!")

                else:
                    print("Invalid Choice!")

    # Book Ticket
    elif choice == "2":
        system.show_buses()

        bus_number = input("\nEnter Bus Number: ")
        name = input("Enter Passenger Name: ")
        phone = input("Enter Phone Number: ")

        system.book_ticket(bus_number, name, phone)

    # View Buses
    elif choice == "3":
        system.show_buses()

    # Exit
    elif choice == "4":
        print("Thank You! Have a Safe Journey.")
        break

    else:
        print("Invalid Choice! Try Again.")
