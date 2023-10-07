import time

def introduction():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a small village, and a wise old man approaches you.")
    time.sleep(1)
    print("He tells you about a legendary treasure hidden in a cave.")
    time.sleep(1)
    print("Do you want to go on a quest to find the treasure? (yes/no)")

def make_choice():
    choice = input().lower()
    if choice == "yes":
        print("Great! You decide to embark on the quest.")
        time.sleep(1)
        cave_quest()
    elif choice == "no":
        print("You decide not to go on the quest. The adventure ends here.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        make_choice()

def cave_quest():
    print("You arrive at the entrance of the cave. It's dark and mysterious.")
    time.sleep(1)
    print("You have two paths to choose from: 'left' or 'right'")
    path_choice = input().lower()
    if path_choice == "left":
        print("You encounter a group of friendly goblins who offer to guide you deeper into the cave.")
        time.sleep(1)
        print("Do you trust them? (yes/no)")
        trust_choice = input().lower()
        if trust_choice == "yes":
            print("The goblins lead you safely to the treasure! Congratulations, you win!")
        elif trust_choice == "no":
            print("You decide not to trust the goblins and continue on your own.")
            time.sleep(1)
            print("Unfortunately, you get lost in the cave and the adventure ends here.")
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            cave_quest()
    elif path_choice == "right":
        print("You encounter a fierce dragon guarding the treasure.")
        time.sleep(1)
        print("Do you want to fight the dragon? (yes/no)")
        fight_choice = input().lower()
        if fight_choice == "yes":
            print("You bravely fight the dragon and manage to defeat it!")
            time.sleep(1)
            print("Congratulations, you have found the legendary treasure. You win!")
        elif fight_choice == "no":
            print("You decide not to fight the dragon. The adventure ends here.")
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            cave_quest()
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        cave_quest()

# Game starts here
introduction()
make_choice()
