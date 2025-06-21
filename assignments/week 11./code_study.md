# Where did you find the code, and why did you choose it? (Provide the link)
game link https://github.com/Grimmys/rpg_tactical_fantasy_game 

I first looked through a few different games like a Piano Tiles game, but most either didn't work or were too simple/short. Since I might want to code an RPG-inspired game for my final assignment, I looked up RPG Python game, and this game came up. I chose it because it looked like a pretty nice and complex game that I could learn from. Additionally, I was looking for a game that uses images and sounds, so that I could get a better idea of how to structure folders and different files.

# What does the program do? What's the general structure of the program?
The program is a turn-based tactical fantasy RPG game where you fight monsters and must deliver an item (ogre bones) to a specific location (far west of the starting point) to win the game. You can buy and trade things, open chests, and talk to NPCs.
The code is organized into several well-structured folders, including the folders: data, fonts, imgs, and maps.

The data folder contains Python files with important game information. One file holds a dictionary of all the fonts used in the game.
Another file includes various texts used throughout the game, such as for the start screen, close button, load game menu, and options menu.
Most of these are strings, but some are functions - for example, those used to display the player's current gold amount.

In the data folder, there is also the folder “zh_cn” with a few XML files. I read a bit about them on Google, but I don't really understand how they work. Are they needed to add another language?
All the images, fonts, and sounds used in the game are sorted into different folders. The maps folder has 4 different subfolders titled level_1, level_2, level_3, and level_4. These contain a bunch of text files with the dialogue used throughout the game, such as the control instructions and characters’ dialogue. The README folder contains md files, all in Chinese, so I actually cannot read it …(っ◞‸◟ c). 
And finally, we get to the actual code files! These are sorted into subfolders in the src folder. The code uses many different classes for different items, characters, and effects (e.g., breakable).
Here are a few examples of the different classes in the code (but not all, because there are so many TT).

Alteration Class: Represents a status effect lasting one or more turns, with attributes like name, abbreviated name, power, duration, and turn tracking.

Character Class: Represents the player or AI-controlled entities. It extends a movable entity with features such as race, class, equipment, skills, and interactions. Characters have stats (HP, strength, defense, resistance) that grow with levels. The class manages equipment, calculates combat effects, and handles dialogue and inventory keys.

Chest Class: Represents chests in the game that can hold items. It has sprites (a two-dimensional image that is part of the larger graphical scene) for closed/open states, an item, and flags for its state. The class uses a static method to probabilistically select items based on weighted chances. The open() method changes the sprite, updates the state, plays a sound effect, and returns the contained item.

# Function analysis: pick one function and analyze it in detail:
## What does this function do?
I chose to analyze the def buy(self, item: Item) -> str: function in the shop.py file. It handles the shop interaction with a player who wants to buy a specific item and returns a different message depending on whether the purchase was successful or not.
The function checks if the player has enough inventory space and gold to buy the item. If that’s the case, it plays a sound effect, deducts the item’s price from the player’s gold, adds the item to the inventory, increases the shop’s gold balance, decreases the item’s quantity in the store, and returns a message saying the purchase was successful.
If the player doesn’t have enough inventory space or gold, it returns a different message based on the reason, and the player is not able to purchase the item.
## What are the inputs and outputs?
Output (Depending on your gold and inventory space):

STR_THE_ITEM_HAS_BEEN_BOUGHT or

STR_NOT_ENOUGH_SPACE_IN_INVENTORY_TO_BUY_THIS_ITEM or

STR_NOT_ENOUGH_GOLD_TO_BY_THIS_ITEM

The only concrete input is the item the player wants to buy. Then there are many other “inputs” that aren't put into the function directly but are required for it to work, like self.current_visitor.gold and self.shop_balance.
## How does it work (step by step)?
This checks if the player has enough gold to purchase the item. If there is not enough gold, it skips to the string at the end, which tells the player they don't have enough gold:

def buy(self, item: Item) -> str:
      if self.current_visitor.gold >= item.price:
      
This compares how many items the player has in their inventory to how many they are allowed to carry. <if their inventory is full, it skips to the string at the end that tells them this:
      
       if len(self.current_visitor.items) < self.current_visitor.nb_items_max:
       
If the player has enough gold and inventory space, the function continues here and plays a sound effect. Then it deducts the item price from the player's gold, adds the item to the inventory, and increases the shop's gold balance:
         
           pygame.mixer.Sound.play(self.gold_sfx)
           self.current_visitor.gold -= item.price
           self.current_visitor.set_item(copy(item))
           self.shop_balance += item.price
           
Here, the shop's inventory gets updated. It removes one of the items, and if the item hits 0, removes it from the shop.:
         
           entry: Optional[dict[str, any]] = self.get_item_entry(item)
           entry["quantity"] -= 1
           if entry["quantity"] <= 0:
               self.stock.remove(entry)
               
Updates the shop menu:
          
           self.update_shop_menu(self.current_visitor.gold)
           
And finally, the ending messages (which depend on the user's gold and inventory space):
          
           return STR_THE_ITEM_HAS_BEEN_BOUGHT
       return STR_NOT_ENOUGH_SPACE_IN_INVENTORY_TO_BUY_THIS_ITEM
   return STR_NOT_ENOUGH_GOLD_TO_BY_THIS_ITEM

# Takeaways: are there anything you can learn from the code?
Since this is a very complex game, there are many things I can learn from the code. However, I’ll summarize the things I learned from it and could realistically use in my own game ( ˶ˆᗜˆ˵ ).
The first thing I noticed was the folder structure - it’s very well organized and clean, making it easy to find what you’re looking for. I liked how text strings are stored in different files, and in the code, it simply says something like return STR_THE_ITEM_HAS_BEEN_BOUGHT. I don’t think this is necessarily needed for simpler games, but for a larger project like this, it definitely made the code easier to navigate and understand. I also liked the use of different .py files for different classes - it keeps everything neat and clear. I also learned about static methods, which are functions inside a class that can be called without creating an instance of that class, and how they can be used to perform tasks like selecting items based on weighted probabilities. Additionally, I learned about sprites, which are 2D images used in games to visually represent characters or objects, and how changing a sprite can show different states, like a chest opening.

# What parts of the code were confusing or difficult to understand?
I'm still a little confused about XML files and how they are used. From what I understand so far, there are methods and functions, such as those using etree, that can save data in XML format. But I'm not completely sure how the process works or when it's typically used.
# Were you able to understand what it is doing after your own research?
I definitely did not understand everything, but I would like to think that I understand most of what I took a closer look at and researched. I didn’t go through every single .py file since there are many, but the ones I did analyze, I think I understood pretty well and can learn a lot from. I spent a lot of time going through and trying to understand the character.py file, since it’s by far one of the - if not the - longest.
# Extra notes
I probably should have chosen a simpler code lol!
But I’m really surprised that with what we’ve learned in class, we can already kind of understand a pretty complex game like this - the basics are all the same! I’m also impressed that a game like this can be made with Python. 

