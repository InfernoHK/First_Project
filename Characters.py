import os
from sys import stdout
from getkey import getkey, keys
from ansi.color import fg
from ansi import cursor
import random
from Player import game_player

 






class NPC:

#Represents a non-player character (NPC) in the game.

#Args:
    #name (str): The name of the NPC.
    #friendly_level (float): The level of friendliness of the NPC, ranging from 0 (hostile) to 1 (friendly).


  def __init__(self, name, friendly_level):
    self.name = name
    self.friendly_level = friendly_level

    
        
class enemy():
  def __init__(self, name, attack_DMG, attack_PW, health):
#
    #Initializes a new instance of the class with the provided name, attack damage, attack power, and health.
    
    #Args:
        #name (str): The name of the character.
        #attack_DMG (float): The base attack damage of the character.
        #attack_PW (float): The attack power modifier of the character.
        #health (float): The initial health of the character.
    
    self.name = name
    self.attack_DMG = attack_DMG
    self.attack_PW = attack_PW
    self.health = health
  def attack(self, target):
    target.health -= (self.attack_DMG + self.attack_PW * 1.2)
    print(f"{self.name} attacks for {self.attack_DMG} damage!")
    


def menu(choices):

#Displays a menu of choices and allows the user to navigate and select an option.

#Args:
    #choices (list): A list of strings representing the menu options.

#Returns:
   # int: The index of the selected menu option (1-based).


  global pos
  pointer = fg.boldblue('>')
  for choice in choices:
    print(choice)
  print(cursor.hide()+cursor.up()*(len(choices))+pointer, end='    ')
  stdout.flush()

  pos = 1
  while 1:
    key = getkey()
    text = f'{""} {choices[pos-1]}'
    if (key == '\x1b[A' or key == 'w') and pos > 1:
      pos -= 1
      print(f'\r{text}\r' + cursor.up() + pointer + \
            fg.bold(f'{""} {choices[pos-1]}'), end = '      ')
    elif (key == '\x1b[B' or key == 's') and pos < len(choices):
      pos += 1
      print(f'\r{text}\r' + cursor.down() + pointer + \
            fg.bold(f'{""} {choices[pos-1]}'), end = '    ')
    elif key == '\n':
      print(cursor.down()*(len(choices)-pos)+cursor.show())
      return pos
    elif key.isdecimal():
      number = int(key)
      if 0 < number <= len(choices):
        print(cursor.down()*(len(choices)-pos)+cursor.show())
        return number
    stdout.flush()

def shop():

#Displays a shop menu where the player can buy and sell items.

#The shop is run by an NPC named Cass, who greets the player with a random message from a list of pre-defined messages. The player can then choose to buy, sell, or leave the shop.

#If the player chooses to buy, they are presented with a list of items they can purchase, including a Health Potion. If the player has enough gold, they can purchase the Health Potion, which is added to their inventory.

#If the player chooses to sell, they are presented with a list of items in their inventory that they can sell.

#If the player chooses to leave, they are returned to the main movement function.


  from Items import Item
  global HealthPotion
  from menusys import menu_sys_list
  from menusys import main_movement
  #John Mcree real name 
  from menusys import new_player
  print("\n")
  os.system("clear")
  beginning25 = ["Hey, Welcome to the shop. I couldnt bother to tell you my name or remember yours for a matter of fact, but you can call me Cass. I'm a shopkeeper, and I'm selling some stuff.","Hello, you can call me Cass, this is my shop, I'm selling some stuff.","Hey, I'm Cass, I'm a shopkeeper, and I'm selling some stuff."]
  beginning50 = ["Hello, welcome back " + new_player.name +"Here's what I got","Hey Friend, Here's What I Got Today"]
  beginning75 = ["Hey It's"]
  shopkeeper = NPC("Cass", 0)
  print(random.choice(beginning25))
  choice = menu(["Buy","Sell","Leave"])
  if choice == 1:
    choice = menu(["Health Potion", "Black Sword", "Cloak", "Leave"])
    if choice == 1:
      if new_player.gold >= 10:
        new_player.gold -= 10
    
        HealthPotion = Item("Health Potion", 0, 0, 5, 25)
        new_player.inventory.append(HealthPotion)
        new_player.inventory.append("test")
        print("You bought a Health Potion")
        print("You have " + str(new_player.gold) + " gold")
        main_movement()
      
      
      else:
        choice = menu(["Buy","Sell","Leave"])
        
  elif choice == 2:
    print("\n")
    print("What do you want to sell?")
    choice = menu(new_player.inventory)
  elif choice == 3:
    print("\n")
    print("Goodbye")
    main_movement()
  
  
  
