import time, sys

# global variables
TEXT_SPEED = 0.05
PINK = "\033[95m"
RESET = "\033[0m"

# Effects
def typingPrint(text, delay=TEXT_SPEED, color=RESET):
    for character in text:
        sys.stdout.write(color + character + RESET)
        sys.stdout.flush()
        time.sleep(delay)
        if character == "\n":
            print()

# NOTE: this game was inspired by my favorite video game Omori :3"

# Functions needed for the mini-games

def is_correct_guess(guess, correct_value):
    return guess == correct_value

# Function for the color game
def color_guess(correct_color, attempts=3):
    valid_colors = ['blue', 'green', 'pink', 'yellow', 'purple', 'white']
    while attempts > 0: # Loop for limited attempts
        guess = input("Your guess: ").strip().lower()

        if guess not in valid_colors:
            print("That's not a valid color. Please choose from Blue, Green, Pink, Yellow, Purple, or White.")
            continue

        if is_correct_guess(guess, correct_color):
            typingPrint("Hero smiles: 'Yes! You do remember!'", color=PINK)
            return True
        else:
            attempts -= 1 # Decrease attempts
            if attempts > 0:
                print(f"Nope... Try again! ({attempts} attempts left)")
            else:
                print("Hero looks a little sad. 'It's okay... maybe next time.'")
                return False

    return False

# Function for the rock riddle
def rock_riddle():
    correct_number = 7
    while True:
        try:
            guess = int(input("Name a number between 1-10: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if guess < 1 or guess > 10:
            print("Seriously...? Stay between 1 and 10.")
        elif is_correct_guess(guess, correct_number):  # Compare players guess with correct_number
            print("Correct! The rock is pleased and lets you pass.")
            break
        else:
            print("Wrong! The rock starts insulting you. Try again.")

# This is where the game starts
def intro_scene():
    print("⠀⠀⢀⣀⣀⣀⣀⡀⠀⡆⠀")
    print("⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣯⠁")
    print("⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆")
    print("⡜⣿⣿⣿⣿⡿⠟⠛⢿⣿⣿⢣")
    print("⠡⣸⠋⢸⠀⠀⠀⠀⡇⠙⣇⠌")
    print("⠀⠀⠈⢲⣀⣀⣀⣀⡖⠁⠀⠀")
    print("⠀⠠⠐⢡⣿⣷⣾⣿⡌⠂⠄⠀")
    print("⠀⠣⠤⡟⡿⢿⡿⢿⢻⠤⠜⠀")
    print("⠀⠀ ⣗⣛⡞⢳⣛⣺⠀⠀⠀")
    print("⠀ ⠀⠹⠟⠁⠈⠻⠏⠀⠀⠀")
    time.sleep(4)
    typingPrint("...")
    time.sleep(1)
    typingPrint("\nWelcome to WHITE SPACE🔪")
    time.sleep(1)
    typingPrint("\nYou have been living here for as long as you can remember.\n")
    time.sleep(2)

# Whitespace
def whitespace_scene(name):
    while True:
        print(f"\n{name}, do you want to leave WHITE SPACE?")
        choice1 = input("'yes' or 'no': ").strip().lower()

        if choice1 == "no":
            print("\nYou stay in WHITE SPACE")
            time.sleep(3)
            print("Time passes slowly...")
            time.sleep(2)
            print("After awhile you begin to feel.. something")
            time.sleep(2)
            print("\n₲₳₥Ɇ ØVɆⱤ") # Game over, the player decided to stay in white space so they dont meet their friends
            break

        elif choice1 == "yes":
            print("\nYou stand up and walk toward the door...")
            time.sleep(2)
            print("You open it and walk into Headspace")
            time.sleep(3)
            friend_scene() # Next scene
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

#Headspace
def friend_scene():
    print("\nYou enter a colorful room. Your friends are waiting for you.")
    time.sleep(2)
    typingPrint("Aubrey: 'We missed you! What should we do today?'\n", color=PINK)
    time.sleep(2)

    print("You think about it...")
    time.sleep(2)
    print("A: Go to the playground")
    time.sleep(2)
    print("B: Explore the forest")
    time.sleep(2)
    print("C: Visit the train station")
    time.sleep(2)

    while True:
        choice2 = input("Choose A, B, or C: ").strip().upper()

        if choice2 == "A":
            playground_scene()
            break

        elif choice2 == "B":
            forest_scene()
            break

        elif choice2 == "C":
            train_scene()
            break

        else:
            print("Invalid choice. Please enter A, B, or C.")

    rock_scene() # Scene after A, B or C
    wakeup_scene()

# if the player chose A = Playground
def playground_scene():
    time.sleep(2)
    print("\nYou arrive at the playground and see some kids play hide and seek. Would you like to join them?")
    time.sleep(2)

    while True:
        choice3 = input("'yes' or 'no': ").strip().lower()

        if choice3 == "yes":
            print("\nYou hide behind a big tree and win the game!")
            break
        elif choice3 == "no":
            print("\nYou walk away. Hide and seek is for children!")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

# if the player chose B = Forest
def forest_scene():
    time.sleep(2)
    print("\nYou walk through the woods and come to a fork in the path")
    time.sleep(2)
    typingPrint("Kel: 'Which way should we go?'\n", color=PINK)
    time.sleep(2)
    print("Left (Bright, pretty path) or Right (Dark, scary looking path)")

    time.sleep(2)

    while True:
        direction = input("Left or Right: ").strip().lower()

        if direction == "right":
            confirm = input("Hero: 'Are you sure?......' (yes/no): ", color=PINK).strip().lower()

            if confirm == "yes":
                print("\nYou head into the darkness...")
                break
            elif confirm == "no":
                print("You turn back to the fork.")
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
        elif direction == "left":
            print("You take the bright, pretty path.")
            break
        else:
            print("Invalid choice. Please enter 'Left' or 'Right'.")

# if the player chose C = Train station
def train_scene():
    time.sleep(2)
    print("\nYou see Basil waiting near the tracks")
    time.sleep(2)
    typingPrint("Basil: 'I think I dropped one of my photos nearby. Can you help me find it?'", color=PINK)
    print()

    while True:
        choice5 = input("'yes' or 'no': ").strip().lower()

        if choice5 == "yes":
            print("You begin looking through the grass...")
            break
        elif choice5 == "no":
            print("Basil looks disappointed. He walks away slowly...")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

# Rock game
def rock_scene():
        time.sleep(2)
        print("\nSuddenly a talking rock blocks your path!!!!")
        typingPrint("Rock: 'Only those who are wise may pass. What number between 1 and 10 am I thinking of?'\n", color=PINK)
        rock_riddle() # Run the mini-game
        color_game() # Scene after mini-game

# Color game
def color_game():
    time.sleep(2)
    print("\nAfter passing the rock, you wander into a quiet flower field.")
    time.sleep(2)
    print("All your friends are sitting there. Hero is sketching in his notebook.")
    time.sleep(2)
    typingPrint("Hero: 'Hey, do you remember my favorite color?'\n" , color=PINK)
    time.sleep(2)
    print("Choices: Blue, Green, Pink, Yellow, Purple, White")

    correct_color = "green" # Set correct answer for mini-game
    color_guess(correct_color) # Start mini-game
    wakeup_scene() # Next scene

# End
def wakeup_scene():
        time.sleep(2)
        typingPrint("\nMari: 'Its getting late. Do you want to wake up?' ˶ᵔ ᵕ ᵔ˶", color=PINK)
        print()

        while True:
            choice6 = input("'yes' or 'no': ").strip().lower()

            if choice6 == "yes":
                print("\nEverything fades. You feel a weird weight in your chest as you open your eyes....")
                time.sleep(3)
                print("\nTHE END.")
                sys.exit()

            elif choice6 == "no":
                print("\nYou sit quietly with your friends as the sun sets.")
                time.sleep(3)
                print("\nTHE END.")
                sys.exit()

            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

# main function
def main():
    intro_scene()
    name = input('What is your name? ')
    whitespace_scene(name)

if __name__ == "__main__":
    main()
