import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand = []

while diamonds:

    random_diamond = random.choice(diamonds)
    option = input("\nPick a card or press Q then Enter to quit.")

    if option.lower == "Q":
        break
    elif option != "Q":
        diamonds.remove(random_diamond)
        hand.append(random_diamond)
        print("Your hand:", str(hand))
        print("Remaining cards:", diamonds)

if not diamonds:
    print("There are no more cards to pick.")
