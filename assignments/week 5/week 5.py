import time, sys

# global variables
TEXT_SPEED = 0.05
PINK = "\033[95m"
RESET = "\033[0m"
current_room = ""
cafe_locked = False
eggs_locked = False
DEBUG = False

# Effects
def typingPrint(text, delay=TEXT_SPEED, color=RESET):
    for character in text:
        sys.stdout.write(color + character + RESET)
        sys.stdout.flush()
        time.sleep(delay)

# --- Game State ---
inventory = []
room_items = {
    "bakery kitchen": [
    {"name": "Magic butter", "type": "ingredient", "description": "Rich and creamy"},
    {"name": "Cupcake", "type": "food", "description": "A sweet snack. Maybe someone would want this?"},
    {"name": "Phone", "type": "tool", "description": "Great to call friends!"}
    ],
    "strawberry field": [
    {"name": "Rotten Strawberries", "type": "ingredient", "description": "These dont look so good anymore..."},
    {"name": "Fresh Strawberries", "type": "ingredient", "description": "Bright red and sweet"}
    ],
    "cinnamoroll café": [
    {"name": "Rainbow Sugar", "type": "ingredient", "description": "Glittery sweet sugar"},
    ],
    "my melody's house": [
    {"name": "Sweet Cream", "type": "ingredient", "description": "Fluffy cream"},
    {"name": "Eggs", "type": "ingredient", "description": "It's her last few eggs..."}
    ],
    "storage room": [
    {"name": "Golden flour", "type": "ingredient", "description": "An essential for all cakes!"},
    ]
}


MAX_INVENTORY_SIZE = 6

# --- Challenges---
def use(item_name):
    global cafe_locked
    global eggs_locked

    item_name = item_name.strip().lower()
    for item in inventory:
        if item["name"].strip().lower() == item_name:
            if item_name == "phone":
                print("\nWho would you like to call?")
                time.sleep(1)
                print("Contacts: My Melody, Badtz-Maru, Cinnamoroll")
                choice=input ("> ").strip().lower()

                if choice == "cinnamoroll":
                    if cafe_locked:
                        print("\n'Hey, I already unlocked it!")
                    else:
                        print("\n'Okay! I will unlock the café for you :3'")
                        cafe_locked = True
                    return
                elif choice == "my melody":
                    print("\n'Hii, I dont have a key to Cinnamorolls Café.. You should probably call him'")
                    return
                elif choice == "badtz-maru":
                    print("\n'What do you want?' *click*")
                    print("Oh... he already hung up.")
                    return
                else:
                    print("That number doesn't work.")
                    return

            elif item_name == "cupcake":
                if current_room == "my melody's house":
                    print("\nMy Melody: That's my favourite!! Thank you so much!")
                    print("She happily takes it.")
                    inventory.remove(item)
                    eggs_locked = True
                else:
                    print("No one here wants a cupcake right now.")
                    return

            elif item["name"].strip().lower() == item_name:
                if item_name in inventory and not "cupcake" or "phone":
                    print(f"You try to use the {item['name']}, but nothing happens.")
                    return
    else:
        print("You don't have that item in your bag.")


# --- Functions ---


def show_inventory():
    if not inventory:
        print("There are just a few old receipts and some loose coins in your bag...")
    else:
        print("\nYou are carrying:")
        for item in inventory:
            print(f"- {item['name']}")

def go_to_room(room_name):
    global current_room
    room_name = room_name.strip().lower()

    with_article = ["strawberry field", "bakery kitchen", "storage room"]

    if room_name in with_article:
        article = "the"
    else:
        article = ""

    if room_name == "cinnamoroll café" and not cafe_locked:
        print(f"\nThe café already closed... If you have a phone, maybe you could call someone to open it?")
        return

    elif room_name == "bakery kitchen":
        current_room = room_name
        print(f"You have entered {article} {current_room}.")
        show_room_items()
        if len(inventory) >= 6:
            print(f"\nDo you think you have all the ingredients in your bag?")

            response = input ("> ").strip().lower()
            if response == "yes":
                check_ingredients()
            elif response == "no":
                print("\nOkay!! Come back once you have everything")
            else:
                print("\nInvalid input. Please try again.")

    elif room_name in room_items:
        current_room = room_name
        print(f"\nYou have entered {article} {current_room}.")
        show_room_items()

    else:
        print("\nThere is no such room.")

# -----

def show_room_items():
    with_article = ["strawberry field", "bakery kitchen", "storage room"]

    if current_room in with_article:
        article = "the"
    else:
        article = ""

    print(f"\nYou are in {article} {current_room}. You see these things laying around:")
    for item in room_items[current_room]:
        print(f"- {item['name']}")

def pick_up(item_name):
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("\nYour bag is already way too heavy! Drop something first")
        return

    if item_name.strip().lower() == "eggs" and not eggs_locked:
        print("\nIt's her last few eggs... Shouldn't you give her something in return?")
        return

    for item in room_items [current_room]:
        if item['name'].strip().lower() == item_name.strip().lower():
            inventory.append(item)
            room_items[current_room].remove(item)
            print(f"You picked up {item['name']}")
            return

    print("There is no such thing here.")

def drop(item_name):
    for item in inventory:
        if item['name'].strip().lower() == item_name.strip().lower():
            inventory.remove(item)
            room_items[current_room].append(item)
            print(f"You dropped {item['name']}")
            return
    print("There is no such thing in your bag.")

def examine(item_name):
    for item in room_items[current_room]:
        if item['name'].strip().lower() == item_name.strip().lower():
            print(f"\n{item['description']}")
            return
    for item in inventory:
        if item['name'].strip().lower() == item_name.strip().lower():
            print(f"\n{item['description']}")
            return
    print(f"\nYou can only examine items in your bag or this room.")

# --- End game ---

def check_ingredients():
    required = ["magic butter", "rainbow sugar", "sweet cream", "fresh strawberries", "golden flour", "eggs"]
    inventory_names = [item["name"].lower() for item in inventory]

    for ingredient in required:
        if ingredient not in inventory_names:
            print(f"You're still missing: {ingredient}")
            return

    print("You have everything! Time to bake the perfect birthday cake! 🎂")
    sys.exit()

# --- Game Loop ---

def game_loop():
    print("""
     ⢀⠤⣀⣀⣴⣶⣔⢂⠀⠀
    ⠀⠸⠀⠀⠀⠻⠿⢿⣿⡇⠀
    ⢀⣸⠀⡀⠀⠀⠀⢠⠀⣗⡂
    ⠀⢚⣄⡁⠀⠛⠀⢀⡰⢷⠀
    ⠀⢠⢎⣿⣿⣭⣽⣿⡄⠜⠀
    ⠀⠘⢺⣿⣿⣿⣿⣿⡇⠀⠀
    ⠀⠀⠐⠤⠤⠼⠤⠤⠄⠀⠀
    """)
    typingPrint("Oh no!!! Hello Kitty forgot about her friend's birthday and only has one day left "
          "\nto bake a delicious special birthday cake, but she doesn't have all the ingredients... "
          "\nCan you help her?"
          "\nOnce you have all the ingredients in your bag please meet her at the bakery kitchen.\n", color=PINK)

    time.sleep(1)

    print("\nType 'help' for a list of commands.")
    print("\nType 'recipe' for a list of the needed ingredients.")
    print("\nType 'map' for map of the available places.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], go [room], quit")
        elif command == "recipe":
            print("Magic butter, Rainbow Sugar, Sweet Cream, Fresh Strawberries, Golden Flour, Eggs")
        elif command == "map" and not cafe_locked:
            print("""
             🍓🍓🍓🍓🍓🍓🍓🍓                              ╱◥█◣
             Strawberry Field 🍓 _ _ _ _🌲___🌳🌳_ _ _ _ _ │ ∩ │ ▓ ║
             🍓🍓🍓🍓🍓🍓🍓🍓          ┃                My Melody's House
             🍓🍓🍓🍓🍓🍓🍓🍓          ┃                                      
                                        ┃
                                        ┃
             Hello Kitty Café :         ┃
             Bakery Kitchen             ┃
             Storage Room┃              ┃                                             
             __________∩___             ┃           ╱◥██◣
           /__\____________\ _ _ _ _🌲___🌳🌳_ _ _ │ ∩ │ ▓ ║ 
           |門 |    田  田   |                Cinnamoroll Café (closed)
           |__ ⚘ ⚘__Π _⚘⚘__ |
            """)
        elif command == "map" and cafe_locked:
            print("""
             🍓🍓🍓🍓🍓🍓🍓🍓                              ╱◥█◣
             Strawberry Field 🍓 _ _ _ _🌲___🌳🌳_ _ _ _ _ │ ∩ │ ▓ ║
             🍓🍓🍓🍓🍓🍓🍓🍓          ┃                My Melody's House
             🍓🍓🍓🍓🍓🍓🍓🍓          ┃                                      
                                        ┃
                                        ┃
             Hello Kitty Café :         ┃
             Bakery Kitchen             ┃
             Storage Room┃              ┃                                             
             __________∩___             ┃           ╱◥██◣
           /__\____________\ _ _ _ _🌲___🌳🌳_ _ _ │ ∩ │ ▓ ║ 
           |門 |    田  田   |                   Cinnamoroll Café
           |__ ⚘ ⚘__Π _⚘⚘__ |
            """)
        elif command.startswith("go "):
            room_name = command[3:].strip()
            go_to_room(room_name)
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:]
            pick_up(item_name)
        elif command.startswith("drop "):
            item_name = command[5:]
            drop(item_name)
        elif command.startswith("use "):
            item_name = command[4:]
            use(item_name)
        elif command.startswith("examine "):
            item_name = command[8:]
            examine(item_name)
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()