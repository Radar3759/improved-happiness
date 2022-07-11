import random

high_score = 0
roll_1 = random.randint(1, 6)
roll_2 = random.randint(1, 6)
print("Current High Score: ", high_score)

def dice_game():
    global high_score
    
    while True:
        print("\nCurrent High Score: ", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        option = input("Enter Your Choice: ")
        if option == "1":
            #roll_1 = random.randint(1, 6)
            #roll_2 = random.randint(1, 6)
            total_roll = roll_1 + roll_2
            print("You roll a...", roll_1)
            print("You roll a...", roll_2)
            print("\nYou have rolled a total of: ", total_roll)
            print("\nNew high score!")
            high_score = high_score + total_roll
        elif option == "2":
            print("Goodbye!")
            break
dice_game()