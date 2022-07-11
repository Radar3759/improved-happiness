
# use print statement
def show_balance(balance):
    print("Your balance is $", float(balance))
# use return statement

def deposit(balance):
    amount = input("Enter amount to deposit: $ ")
    return (balance + float(amount))
# use return statement
# bonus check to see if there's enough to withdraw

def withdraw(balance):
    amount = input("Enter amount to withdraw: $ ")
    if float(amount) > balance:
        print("That is more than the current balance")
    else:
        return (balance - float(amount))
# use print statement

def logout(name):
    print("Goodbye", name)
