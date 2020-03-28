users = {}
status = ""

def displayMenu():
    status = input("Are you a register user? (y/n) Press q to quit.\n")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
    elif status == "q":
        while True:
            break

def newUser():
    createLogin = input("Create login name:\n")

    if createLogin in users:
        print("\nLogin name already exists.\n")
    else:
        createPassword = input("Create a password:\n")
        users[createLogin] = createPassword
        print("\nUser created.\n")

def oldUser():
    login = input("Enter your login name:\n")
    password = input("Enter your password:\n")

    if login in users and users[login] == password:
        print("\nYou have successfully logged into your account.")
    else:
        print("\nError. Invalid credentials. Please try again.")

displayMenu()
