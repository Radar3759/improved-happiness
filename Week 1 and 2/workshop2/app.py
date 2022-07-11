# Task 1, Task 2 Task 3 Task 4complete
from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("\n          === Automated Teller Machine ===          ")
# limit username to 10 characters
while True:
    name = input("Enter name to register: ")
    if len(name) > 10:
        print("The maximum name length is 10 characters.")
    else:
        break
# pin must be 4 characters
while True:
    pin = input("Enter PIN: ")
    if len(pin) < 4:
        print("A PIN must be 4 numbers")
    else:
        break

balance = 0
print(name, "has been registered with a starting balance of $", str(balance))

while True:
    print("\nLOGIN")
    name_to_validate = input("Enter your name: ")
    pin_to_validate = input("Enter your PIN: ")

    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful")
        break
    else:
        print("Invalid credentials")

while True:

    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        print("Your balance is now: $", balance)
    elif option == "3":
        balance = account.withdraw(balance)
        print("Your balance is now: $", balance)
    elif option == "4":
        account.logout(name)
        break
    else:
        print("You didn't pick between 1-4")
        break
