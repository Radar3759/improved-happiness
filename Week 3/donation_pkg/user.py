#Task 4
def login(database, username, password):
    database = { }
    for username, password in database.items(username, password):
        if 'admin' in username and 'password' in password:
            print("Welcome, ", username)
        else:
            print("Login Failed.")
            
