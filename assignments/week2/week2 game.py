import time, sys

def typingPrint(text):
   for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)

      if character == "\n":
        print()

print("NOTE: this game was inspired by my favorite video game Omori :3")
time.sleep(2)
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

name = input('What is your name?')

time.sleep(2)
print("\n"+name+", do you want to leave WHITE SPACE?")
choice1 = input("'yes' or 'no'")

if choice1 == "no":
    print("\nYou stay in WHITE SPACE")
    time.sleep(3)
    print("Time passes slowly...")
    time.sleep(2)
    print("After awhile you being to feel.. something")
    time.sleep(2)
    print("\n₲₳₥Ɇ ØVɆⱤ")

elif choice1 == "yes":
    print("\nYou stand up and walk toward the door...")
    time.sleep(2)
    print("You open it and walk into Headspace")

    time.sleep(3)
    print("\nYou enter a colorful room. Your friends are waiting for you.")
    time.sleep(2)
    typingPrint("Aubrey: 'We missed you! What should we do today?'\n")
    time.sleep(2)

    print("You think about it...")
    time.sleep(2)
    print("A: Go to the playground")
    time.sleep(2)
    print("B: Explore the forest")
    time.sleep(2)
    print("C: Visit the train station")
    time.sleep(2)

    choice2 = input("Choose A, B, or C: ")

    if choice2 == "A":
        time.sleep(2)
        print("\nYou arrive at the playground and see some kids play hide and seek. Would you like to join them?")
        time.sleep(2)
        choice3 = input("'yes' or 'no': ")

        if choice3 == "yes":
            print("\nYou hide behind a big tree and win the game!")
        elif choice3 == "no":
            print("\n You walk away. Hide and seek is for children!")

    elif choice2 == "B":
        time.sleep(2)
        print("\nYou walk through the woods and come to a fork in the path")
        time.sleep(2)
        typingPrint("Kel: 'Which way should we go?'\n")
        time.sleep(2)
        print("Left (Bright, pretty path or Right (Dark, scary looking path)")

        time.sleep(2)
        direction = input("'Left' or 'Right?'")

        if direction == "Right":
            confirm = input("Hero: 'Are you sure?......' (yes/no): ")

            if confirm == "yes":
                print("\nYou head into the darkness...")
            else:
                print("You turn back to the fork.")

    elif choice2 == "C":
        time.sleep(2)
        print("\nYou see Basil waiting near the tracks")
        time.sleep(2)
        typingPrint("Basil: 'I think I dropped one of my photos nearby. Can you help me find it?'")
        print()

        choice5 = input("'yes' or 'no': ")

        if choice5 == "yes":
            print("You begin looking through the grass...")
        elif choice5 == "no":
            print("Basil looks disappointed. He walks away slowly...")

    time.sleep(2)
    print("\nSuddenly a talking rock blocks your path!!!!")
    time.sleep(3)
    typingPrint("Rock: 'Only those who are wise may pass. What number between 1 and 10 am I thinking of?'\n")
    time.sleep(3)

    while True:
        riddle = int(input("Name a number between 1-10: "))

        if riddle < 1 or riddle > 10:
            print("Seriously...?")
        elif riddle == 7:
            print("Correct! The rock is pleased and lets you pass.")
            break
        else:
            print("\nWrong! The rock starts insulting you. Try again.")

    time.sleep(2)
    typingPrint("\nMari: 'Its getting late. Do you want to wake up?' ˶ᵔ ᵕ ᵔ˶")
    print()
    choice6 = input("'yes' or 'no': ")

    if choice6 == "yes":
        print("\nEverything fades. You feel a weird weight in your chest as you open your eyes....")
        time.sleep(10)
    elif choice6 == "no":
        print("\nYou sit quietly with your friends as the sun sets.")
        time.sleep(10)




