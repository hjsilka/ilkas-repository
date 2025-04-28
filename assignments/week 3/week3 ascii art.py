import time, sys, random

def typingPrint(text):
   for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)

print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠤⠒⠀⠈⠓⠠⠐⠢⠄⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⠠⠤⠀⠀⠄⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠦⠤⠒⠒⠒⠠⣀⠀
⠀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣣
⣔⠀⠤⠄⣀⣀⠀⠀⠀⠀⠀⠀⣠⡂⠀⠀⠀⠲⣄⣀⠀⠀⠀⠀⢀⡤⠒⠈⠀
⠀⠀⠀⠀⠀⠌⠀⠀⠀⢠⠖⣁⡀⠈⠀⠀⠀⡌⢠⣄⠑⡄⠀⠀⠉⠂⠀⠀⠀
⠀⠀⠀⠀⡜⠀⠀⠀⢠⠃⢸⣿⣽⠀⠀⠀⠀⠇⢿⣷⠇⠘⠀⠀⠀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⡄⠀⠀⠀⠀⠈⠑⠒⠉⠀⢀⡴⣀⠀⠀⠉⠐⠁⠀⠀⠀⡀⠀⠀⠀
⠒⠒⠒⠂⠘⡀⠐⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠐⠒⠀⠠⠤⠃⠤⠠⠄
⠀⠀⠀⠀⠀⢘⣤⠌⠀⠀⠀⠀⠀⠀⠐⠒⠂⠀⠀⠀⠁⠒⠤⡴⢁⣀⠀⠀⠀
⠀⠀⠒⠂⠈⠀⠀⠱⡴⠉⠑⠉⡵⠂⠀⠀⠀⡔⢲⠒⠖⠒⠊⠀⠀⠀⠉⠉⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠣⠴⢇⡠⠅⠘⠉⠉⠁⢄⣀⣠⣀⠄⠀⠀⠀⠀⠀⠀⠀

""")
typingPrint("Hi there! My cat is looking for a date for valentines day. "
      "Could you help her impress someone with some flowers? (˶˃ ᵕ ˂˶)")
print()

time.sleep(2)

print("\nThis is the cat that she likes:")

time.sleep(2)

other_cats = ["Tom", "Claire","Hendrik", "Julia", "Larry"]
random_cat = random.choice(other_cats)
print(random_cat)
print("⋆𐙚₊˚⊹♡")

male_cats = ["Tom", "Hendrik", "Larry"]
female_cats = ["Claire", "Julia"]

if random_cat not in male_cats:
    gender = "her"
elif random_cat in male_cats:
    gender = "him"

if random_cat not in male_cats:
    gender_two = "she"
elif random_cat in male_cats:
    gender_two = "he"

time.sleep(2)

while True:
    try:
        flowers = int(input(f"\nHow many flowers do you think my cat needs to bring to impress {gender}?: "))

        if flowers > 16:
            print("\nWoah! That is a lot of flowers. My cat doesn't have enough dabloons to afford this many. Please try again.")
        elif flowers < 10:
            print(f"\nUhm... I dont think {gender_two} would be very impressed. Please try again.")
        else:
            print(f"\nGreat! My cat will bring {flowers} flowers.")
            break
    except ValueError:
        print("\nAre you trying to sabotage my cat? Please enter a number.")

time.sleep(2)

flower_type = input("\nWhat kind of flowers should she bring? (e.g., roses, sunflowers, tulips, cherry blossom):")
print(f"\nMy cat is going to bring {flowers} {flower_type} just for {gender}.")

if "roses" in flower_type.strip().lower():
    emoji = "🌹"
elif "sunflowers" in flower_type.strip().lower():
    emoji = "🌻"
elif "tulips" in flower_type.strip().lower():
    emoji = "🌷"
elif "cherry blossom" in flower_type.strip().lower():
    emoji = "🌸"
else:
    emoji = "💐"


time.sleep(2)

pickup_line = input("\nAlmost ready! Now what pickup line should my cat use?:")

while True:
    artist = input(f"\nShe would also like to play a song. What artist do you think {random_cat} likes: "
                   f"Taylor Swhiskers or Snoop Cat? ").strip().lower()

    if artist == "taylor swhiskers":
            try:
                song = int(input("Song '1' (Enchanted) or '2' (Lover)? ").strip())
                if song == 1:
                    print("\n     Enchanted")
                    print("⇄      ◀ 𓊕 ▶    ↻")
                    break
                elif song == 2:
                    print("\n       Lover")
                    print("⇄      ◀ 𓊕 ▶    ↻")
                    break
                else:
                    print("That song is not on her playlist, sorry... Try again!")
            except ValueError:
                print("Please enter a number (1 or 2)!")

    elif artist == "snoop cat":
            try:
                song = int(input("Song '1' (Beautiful) or '2' (Sensual Seduction)? ").strip())
                if song == 1:
                    print("\n     Beautiful")
                    print("⇄      ◀ 𓊕 ▶    ↻")
                    break
                elif song == 2:
                    print("\n Sensual Seduction")
                    print("⇄      ◀ 𓊕 ▶    ↻")
                    break
                else:
                    print("That song is not on his playlist, sorry... Try again!")
            except ValueError:
                print("Please enter a number (1 or 2)!")
    else:
        print("My cat is not familiar with this artist...")


# finished ascii art cat! ^^
print("\n")

flowers_per_row = 4
first_row_flowers = flowers % flowers_per_row

count = 0

if first_row_flowers != 0: # first row

    for i in range(first_row_flowers):
        print(emoji, end=' ')
        count += 1
    print()

while count < flowers: # other rows
    for i in range(flowers_per_row):
        if count < flowers:
            print(emoji, end=' ')
            count += 1
    print()
print(" \        /  ⡏⠐⢌⡙⠲⣄⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠛⣛⢳ ")
print("  \      /  ⠀⡇⠀⠀⠑⡄⠼⠗⠒⠒⠒⠒⠿⠁⢀⠔⠋⢀⠀⡇")
print("    ──🎀    ⠀⣧⠀⠠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⣾")
print("  /      \  ⠀⢹⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣴⠇")
print(" /        \ ⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿")
print("   ──────     ⢸⡇⠀⠀⠶⢦⡀⠀⠀⠀⢀⣠⡤⠀⠀⠀⠀⠀⣿")
print("⠀            ⠤⢷⢒⣲⡄⠀⠀⣄⣄⡤⠈⠀⠀⣴⣒⢲⠯⠄")
print("⠀              ⠈⠉⠳⢦⣤⠖⠛⢲⠀⠀⠀⢀⣀⣤⠶⠋⠉")
print("        ⠀⠀⠀       ⠀⡏⠀⢿⠋⠉⠉⠉⠉⠙⣦")
print("⠀⠀⠀              ⠀⠀⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧")
print("⠀⠀⠀               ⠀⠀⣿⠆⠀⠀⡇⠀⢠⠀⠀⢸⣇")
print("⠀⠀⠀               ⠀⠀⡿⠀⠀⠀⡇⠀⣟⡀⠀⣸⣍⢳⡄")
print("⠀⠀⠀⠀              ⠀⠀⠓⠒⠒⠺⣅⣴⠿⠥⣼⠗⣋⡼⠁")
print(" ⠀⠀⠀⠀⠀⠀⠀⠀             ⠀⠀⠀⠀⠀⠀⠉⠉⠉")

print("Cat:" + pickup_line)
print("(ﾐචᆽචﾐ)")

time.sleep(2)

print()
typingPrint("\nGood job! Thank you for helping my cat out ◝(ᵔᗜᵔ)◜")