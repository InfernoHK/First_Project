from Characters import menu
import os
from Player import game_player
from Characters import shop
import random
global menu_sys_list 
menu_sys_list = []
global turn_timer 


def end_day():
        new_player.day += 1
        new_player.actions = 0
        print("You have Rested at the inn and started a new day, It is now day " + str(new_player.day))
        main_movement()

def main_menu():
   
    if menu_sys_list == []:
        
        choice = menu(["Start","Options", "Controls","Exit", "Credits"])
        if choice == 1:
            menu_sys_list.append("Start")
            Start()
            
        elif choice == 2:
            menu_sys_list.append("Options")
            Options()
            
        elif choice == 3:
            menu_sys_list.append("Controls")
            Controls()
            
        elif choice == 4:
            menu_sys_list.append("Exit")
            Exit()
            
        elif choice == 5:
            menu_sys_list.append("Credits")
            Credits()
            
    else:
        choice = menu(["Options", "Controls","Exit", "Credits", "Inventory"])
        if choice == 1:
            menu_sys_list.append("Options")
            Options()
        elif choice == 2:
            menu_sys_list.append("Controls")
            Controls()
        elif choice == 3:
            menu_sys_list.append("Exit")
            Exit()
        elif choice == 4:
            menu_sys_list.append("Credits")
            Credits()
        elif  choice == 5:
            menu_sys_list.append("Inventory")
            Inventory()

      
def Start ():
    os.system('clear')
    global new_player
    print("You awake in this world, you don't know who you are, or where you are from. You don't know anything about this world. You don't even know your name. You are just a stranger in a strange land.")
   
    new_player = game_player("", 100, [], 0, 10, 25)
    print("Okay " + new_player.name + " Welcome, Let me tell you a little about this world. It is a world filled with magic and excitment")
    print("\n")
    print(new_player.actions)

    main_movement()
    print(new_player.actions)
    print(menu_sys_list)


def Options():
    os.system('clear')
    print("No Options Currently Available")
    print("\n")
    if menu_sys_list == []:
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
    else:
        choice = menu(["Options", "Controls","Exit", "Credits"])
        if choice == 1:
            menu_sys_list.append("Options")
            Options()
        elif choice == 2:
            menu_sys_list.append("Controls")
            Controls()
        elif choice == 3:
            menu_sys_list.append("Exit")
            Exit()
        elif choice == 4:
            menu_sys_list.append("Credits")
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
    choices = ["Shop", "Dungeon", "Inn", "Main Menu", "Inventory"]
    choice = menu(choices)
    print(choice)
    if choice == 4:
            main_menu()
    elif new_player.actions < 5:
        if choice == 1:
            new_player.actions += 1
            shop()
        
            
        elif choice == 2:
            new_player.actions += 1
            print("You have entered the dungeon")
            dungeon()
        

    
        elif choice == 3:
            end_day()
            print("You have entered the inn")

        elif choice == 5:
            Inventory()

    elif new_player.actions == 5:
        if choice == 3:
            end_day()
            print("You have entered the inn")
        else:
            print("You Have run out of actions for the day please rest at the inn")
            main_movement()
    
def Inventory():
    os.system('clear')
    print(" You Have the Follwing items")
    for thing in new_player.inventory:
        print(str(thing.name))
    print("\n")
   
    print("You have " + str(new_player.gold) + " gold")
    print("You have " + str(new_player.health) + " health")
    print("Would you like to use any items? ")
    choice = menu(["Yes", "No"])
    if choice == 1:
        print("What would you like to use? ")
        
        choice = menu([new_player.inventory])
        if choice == 1:
            new_player.health += 10
            new_player.inventory.remove(new_player.inventory[0])
            
       

    choice = menu(["Main Menu", "Town", "Exit"])
    if choice == 1:
        main_menu()
    elif choice == 2:
        main_movement()
    elif choice == 3:
        exit()

def dungeon():
    import random
    from Characters import enemy
    enemy_list = []
    goblin = enemy("Globin", random.randint(5,20), random.randint(1,10), random.randint(5,50))

    enemy_list.append(goblin)
    enemy_list.append(goblin)
    enemy_list.append(goblin)
    enemy_first = random.choice(enemy_list)
    print("You encounter a " + enemy_first.name)
    print(" It has " + str(enemy_first.health) + " Health, " + str(enemy_first.attack_DMG) + " AD " + str(enemy_first.attack_PW) + " AP")

