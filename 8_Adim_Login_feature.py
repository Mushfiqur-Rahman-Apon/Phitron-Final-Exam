
class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"
        self.logged_in = False

    # Login Method
    def login(self, username, password):

        if username == self.username and password == self.password:
            self.logged_in = True
            print("\nLogin Successful!")
            return True

        else:
            print("\nInvalid Username or Password!")
            return False

    # Admin Menu
    def admin_menu(self):

        if self.logged_in:
            while True:
                print("\n===== ADMIN MENU =====")
                print("1. Add Bus")
                print("2. View Buses")
                print("3. Logout")

                choice = input("Enter Choice: ")

                if choice == "1":
                    print("Add Bus Selected!")

                elif choice == "2":
                    print("View Buses Selected!")

                elif choice == "3":
                    self.logged_in = False
                    print("Admin Logged Out!")
                    break

                else:
                    print("Invalid Choice!")

        else:
            print("Access Denied! Please Login First.")


# Main Program
admin = Admin()

print("===== ADMIN LOGIN =====")

username = input("Enter Username: ")
password = input("Enter Password: ")

if admin.login(username, password):
    admin.admin_menu()
