#up to task 3 works
'''useful docstring'''
from donation_pkg import homepage
from donation_pkg import user
#declare a var named database
#assign key:value pair 
database = {
    'admin': 'admin',
    'password': 'password123'
}
donations = {}
authorized_user = " "
homepage.show_homepage()

if authorized_user == " ":
    print("You must be logged in to donate.")
else:
    print(f"Logged in as:", {authorized_user})

option = input("Choose an option 1-5: ")

while True:
    if option == "1":
        print("TODO: Write Login Functionality")
    elif option == "2":    
        print("TODO: Write Register Functionality")
        
    elif option == "3":
        print("TODO: Write Donate Functionality")
        # option = input("Choose an option 1-5: ")
    elif option == "4":
        print("TODO: Write Show Donations Functionality")
        # option = input("Choose an option 1-5: ")
    elif option == "5":
        print("Goodbye!")
        break
#test Task 3
    option = input("Pick again: ")

