import os
from sys import stdout
from getkey import getkey, keys
from ansi.color import fg
from ansi import cursor
import random
from Player import game_player
from menusys import main_menu 
import menusys





class NPC:
    def __init__(self, name, friendly_level):
        self.name = name
        self.friendly_level = friendly_level

    def talk_to_player(self, player_name):
        print()
        
class enemy():
    def __init__(self, name, attack_DMG, attack_PW):
        self.name = name
        self.attack_DMG = attack_DMG
        self.attack_PW = attack_PW


def menu(choices):
  global pos
  pointer = fg.boldblue('>')
  for choice in choices:
    print(choice)
  print(cursor.hide()+cursor.up()*(len(choices))+pointer, end='   ')
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
  #John Mcree real name 
  print("\n")
  print(menusys.menu_sys_list)
  beginning25 = ["Hey, Welcome to the shop. I couldnt bother to tell you my name or remember yours for a matter of fact, but you can call me Cass. I'm a shopkeeper, and I'm selling some stuff.","Hello, you can call me Cass, this is my shop, I'm selling some stuff.","Hey, I'm Cass, I'm a shopkeeper, and I'm selling some stuff."]
  beginning50 = ["Hello, welcome back " + menusys.new_player.name +"Here's what I got","Hey Friend, Here's What I Got Today"]
  beginning75 = ["Hey It's"]
  print(random.choice(beginning25))
  main_movement()
  
