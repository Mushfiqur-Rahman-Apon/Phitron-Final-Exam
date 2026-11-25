class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
            print("Login Successful!")
        else:
            print("Invalid Username or Password!")


# Create Admin object
admin1 = Admin("apon", "12345")

# User input
username = input("Enter Username: ")
password = input("Enter Password: ")

# Check login
admin1.login(username, password)