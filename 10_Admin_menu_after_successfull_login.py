
class Bus:
    def __init__(self, number, route, seats):
        self.number = number
        self.route = route
        self.seats = seats


class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"
        self.logged_in = False

    # Admin Login
    def login(self, username, password):
        if username == self.username and password == self.password:
            self.logged_in = True
            print("Login Successful!")
            return True
        else:
            print("Invalid Username or Password!")
            return False


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
        if not self.buses:
            print("No Buses Available!")
            return

        print("\n===== ALL BUSES =====")

        for bus in self.buses:
            print("Bus Number:", bus.number)
            print("Route:", bus.route)
            print("Available Seats:", bus.seats)
            print("--------------------")


# Create Objects
admin = Admin()
system = BusManagement()


# Admin Menu
def admin_menu():

    if not admin.logged_in:
        print("Access Denied! Please Login First.")
        return

    while admin.logged_in:

        print("\n====== ADMIN MENU ======")
        print("1. Add Bus")
        print("2. View All Buses")
        print("3. Logout")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            number = input("Enter Bus Number: ")
            route = input("Enter Bus Route: ")
            seats = int(input("Enter Total Seats: "))

            system.add_bus(number, route, seats)

        elif choice == "2":
            system.show_buses()

        elif choice == "3":
            admin.logged_in = False
            print("Admin Logged Out Successfully!")

        else:
            print("Invalid Choice! Try Again.")


# Main Program
username = input("Enter Username: ")
password = input("Enter Password: ")

if admin.login(username, password):
    admin_menu()
