'''useful docstring'''
#Task 4
#define a f(x) login
#three params database, username, password
def login(database, username, password):
    database = { }
    for username, password in database.items(username, password):
        if 'username' in username and 'password' in password:
            print("Welcome, ", username)
            return username
        else:
            print("Login Failed.")
            return ' '
            
