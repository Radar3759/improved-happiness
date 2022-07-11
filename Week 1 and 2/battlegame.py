# includes Bonus 1-3
wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"


wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 200

wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 30

dragon_hp = 300
dragon_damage = 50

while True:
    print("1. Wizard")
    print("2. Elf")
    print("3. Human")
    print("4. Orc")

    option_1 = input("Choose your character: ")
    option = option_1.lower()

    if option == "1" or option == "wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage

    elif option == "2" or option == "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage

    elif option == "3" or option == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
    elif option == "4" or option == "orc":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
    else:
        print("Unknown Character")
    break

print("You have chosen the character: " + character)
print("Health: " + str(my_hp))
print("Damage: " + str(my_damage))

while True:
    dragon_hp = (dragon_hp - my_damage)
    my_hp = (my_hp - dragon_damage)
    print("\nThe " + character + " damaged the Dragon!")
    if dragon_hp > 0:
        print("The Dragon's hitpoints are now: " + (str(dragon_hp)))
        print("\nThe Dragon strikes back at the " + character)
    else:
        print("The Dragon's hitpoints are now: " + (str(dragon_hp)))
        print("\nThe Dragon has lost the battle.")
        break

    if my_hp > 0:
        print("The " + character+"'s hitpoints are now: " + (str(my_hp)))
    else:
        print("The " + character+"'s hitpoints are now: " + (str(my_hp)))
        print("\nThe " + character + " has lost the battle.")
        break
