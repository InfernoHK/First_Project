from Characters import menu
import os
from Player import game_player
menu_sys = []
global turn_timer 

def main_menu():
    while menu_sys == []:
        menu_sys.append(main_menu)
        choice = menu(["Start","Options", "Controls","Exit", "Credits"])
        if choice == 1:
            menu_sys.append(Start)
            Start()
            break
        elif choice == 2:
            menu_sys.append(Options)
            Options()
            
        elif choice == 3:
            menu_sys.append(Controls)
            Controls()
            
        elif choice == 4:
            menu_sys.append(Exit)
            Exit()
            
        elif choice == 5:
            menu_sys.append(Credits)
            Credits()
            
    

      
def Start ():
    os.system('clear')
    new_player = game_player("", 100, [], 0, 10, 25)
    print("Okay " + new_player.name + " Welcome, Let me tell you a little about this world. It is a world filled with magic and excitment")
    main_movement()
    print(menu_sys)


def Options():
    os.system('clear')
    print("No Options Currently Available")
    print("\n")
    choice = menu(["Start","Options", "Controls","Exit", "Credits"])
    if choice == 1:
        menu_sys.append(start)
        Start()
        
    elif choice == 2:
        menu_sys.append(Options)
        Options()
            
    elif choice == 3:
        menu_sys.append(Controls)
        Controls()
            
    elif choice == 4:
        menu_sys.append(Exit)
        Exit()
            
    elif choice == 5:
        menu_sys.append(Credits)
        Credits()

def Controls():
    os.system('clear')
    print("No Controls Or Keybind Remapping Currently Available")
    print("Press Any Key to Continue When Dialouge is Done")
    print("Arrow Keys to Maneuver Choice Selection")
    print("Enter to Select Choice")
    print("Type Inventory when in game to view your inventory")
    print("\n")
    choice = menu(["Start","Options", "Controls","Exit", "Credits"])
    if choice == 1:
        menu_sys.append(start)
        Start()
        
    elif choice == 2:
        menu_sys.append(Options)
        Options()
            
    elif choice == 3:
        menu_sys.append(Controls)
        Controls()
            
    elif choice == 4:
        menu_sys.append(Exit)
        Exit()
            
    elif choice == 5:
        menu_sys.append(Credits)
        Credits()

def Exit():
    os.system('clear')
    print("Exiting Game")
    exit()

def Credits():
    os.system('clear')
    print("Created By:")
    print ("Futuluhtoogan")
    pause = input()
    print("With the heelp of:")
    print("The Jittleyang Community")
    pause = input()
    pause = input()
    team = input("Are you a Jittleyang or a Futuluhtoogan? ")
    print("\n")
    choice = menu(["Start","Options", "Controls","Exit", "Credits"])
    if choice == 1:
        menu_sys.append(start)
        Start()
        
    elif choice == 2:
        menu_sys.append(Options)
        Options()
            
    elif choice == 3:
        menu_sys.append(Controls)
        Controls()
            
    elif choice == 4:
        menu_sys.append(Exit)
        Exit()
            
    elif choice == 5:
        menu_sys.append(Credits)
        Credits()

def main_movement():
    print("\n")
    choices = ["Shop", "Dungeon", "Inn", "Main Menu"]
    if menu(choices) == 1:
        shop()