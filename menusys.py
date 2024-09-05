from Characters import menu
import os
from Player import game_player
from Characters import shop
global menu_sys_list 
menu_sys_list = []
global turn_timer 

def main_menu():
    
    while menu_sys_list == []:
        menu_sys_list.append(main_menu)
        choice = menu(["Start","Options", "Controls","Exit", "Credits"])
        if choice == 1:
            menu_sys_list.append(Start)
            Start()
            break
        elif choice == 2:
            menu_sys_list.append(Options)
            Options()
            
        elif choice == 3:
            menu_sys_list.append(Controls)
            Controls()
            
        elif choice == 4:
            menu_sys_list.append(Exit)
            Exit()
            
        elif choice == 5:
            menu_sys_list.append(Credits)
            Credits()
            
    choice = menu(["Options", "Controls","Exit", "Credits"])
    if choice == 1:
        menu_sys_list.append(Options)
        Options()
    elif choice == 2:
        menu_sys_list.append(Controls)
        Controls()
    elif choice == 3:
        menu_sys_list.append(Exit)
        Exit()
    elif choice == 4:
        menu_sys_list.append(Credits)
        Credits()

      
def Start ():
    os.system('clear')
    
    print("You awake in this world, you don't know who you are, or where you are from. You don't know anything about this world. You don't even know your name. You are just a stranger in a strange land.")
    global new_player
    new_player = game_player("", 100, [], 0, 10, 25)
    print("Okay " + new_player.name + " Welcome, Let me tell you a little about this world. It is a world filled with magic and excitment")
    print("\n")
    
    main_movement()
    print(menu_sys_list)


def Options():
    os.system('clear')
    print("No Options Currently Available")
    print("\n")
    choice = menu(["Start","Options", "Controls","Exit", "Credits"])
    if choice == 1:
        menu_sys_list.append(Start)
        Start()
        
    elif choice == 2:
        menu_sys_list.append(Options)
        Options()
            
    elif choice == 3:
        menu_sys_list.append(Controls)
        Controls()
            
    elif choice == 4:
        menu_sys_list.append(Exit)
        Exit()
            
    elif choice == 5:
        menu_sys_list.append(Credits)
        Credits()

def Controls():
    os.system('clear')
    print("No Controls Or Keybind Remapping Currently Available")
    print("Press Any Key to Continue When Dialouge is Done")
    print("Arrow Keys to Maneuver Choice Selection")
    print("Enter to Select Choice")
    print("Select Inventory to Open Inventory")
    print("\n")
    choice = menu(["Start","Options", "Controls","Exit", "Credits"])
    if choice == 1:
        menu_sys_list.append(Start)
        Start()
        
    elif choice == 2:
        menu_sys_list.append(Options)
        Options()
            
    elif choice == 3:
        menu_sys_list.append(Controls)
        Controls()
            
    elif choice == 4:
        menu_sys_list.append(Exit)
        Exit()
            
    elif choice == 5:
        menu_sys_list.append(Credits)
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
        menu_sys_list.append(Start)
        Start()
        
    elif choice == 2:
        menu_sys_list.append(Options)
        Options()
            
    elif choice == 3:
        menu_sys_list.append(Controls)
        Controls()
            
    elif choice == 4:
        menu_sys_list.append(Exit)
        Exit()
            
    elif choice == 5:
        menu_sys_list.append(Credits)
        Credits()

def main_movement():
    print("\n")
    choices = ["Shop", "Dungeon", "Inn", "Main Menu","Back"]
    if menu(choices) == 1:
        if new_player.actions < 5:
            new_player.actions += 1
            shop()
        else:
            print("The Shop is Currently Closed")
    elif choices == 2:
        if new_player.actions < 5:
            new_player.actions += 1
            print("You have entered the dungeon")
            #dungeon func
        else:
            print("Your are too tired to enter the dungeon")

    
    elif choices == 3:
        end_day()
        print("You have entered the inn")
    elif choices == 4:
        print()
        #inn func
    elif choices == 5:
        main_menu()
    
    def end_day():
        new_player.day += 1
        new_player.actions = 0
        print("You have Rested at the inn and started a new day, It is now day " + str(new_player.day))
        main_movement()