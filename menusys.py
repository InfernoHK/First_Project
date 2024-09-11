from Characters import menu
import os
from Player import game_player
from Characters import shop
import random
global menu_sys_list 
menu_sys_list = []
global turn_timer 


def end_day():

#Ends the current day, incrementing the player's day counter, resetting their actions, restoring their health to 100, and calling the main_movement() function to continue the game.


    new_player.day += 1
    new_player.actions = 0
    print("You have Rested at the inn and started a new day, It is now day " + str(new_player.day))
    new_player.health = 100
    main_movement()

def main_menu():

#Displays the main menu options and handles user input to navigate to different parts of the game.

#If the menu_sys_list is empty, it will display the full main menu with options to start the game, access options, controls, exit, and view credits.

#If the menu_sys_list is not empty, it will display a reduced menu with options to access options, controls, exit, credits, and the player's inventory.

#The function will append the selected option to the menu_sys_list and then call the corresponding function to handle that option.


   
    if menu_sys_list == []:
        
        choice = menu(["Start","Options", "Controls","Exit", "Credits"])
        if choice == 1:
            menu_sys_list.append("Start")
            Start()
            
        elif choice == 2:
            
            Options()
            
        elif choice == 3:
            
            Controls()
            
        elif choice == 4:
            menu_sys_list.append("Exit")
            Exit()
            
        elif choice == 5:
            
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

#The `Start()` function is responsible for initializing the game and setting up the player character. It performs the following tasks:

#1. Clears the console screen using `os.system('clear')`.
#2. Initializes a new game player object with default values for name, health, inventory, level, strength, and agility.
#3. Prints a welcome message to the player, introducing them to the world and their character.
#4. Calls the `main_movement()` function to start the game.
#5. Prints the player's current actions and the `menu_sys_list` to the console.


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

#The `Options()` function is responsible for displaying the game's options menu and handling user input. It performs the following tasks:

#1. Clears the console screen using `os.system('clear')`.
#2. Prints a message indicating that no options are currently available.
#3. Checks if the `menu_sys_list` is empty. If it is, it displays the main menu options (Start, Options, Controls, Exit, Credits) and handles the user's choice accordingly, appending the selected function to the `menu_sys_list`.
#4. If the `menu_sys_list` is not empty, it displays a different set of options (Options, Controls, Exit, Credits) and handles the user's choice accordingly, appending the selected function to the `menu_sys_list`.


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

#The `Controls()` function is responsible for displaying the game's controls and keybinding information. It performs the following tasks:

#1. Clears the console screen using `os.system('clear')`.
#2. Prints a message indicating that no controls or keybind remapping are currently available.
#3. Prints instructions for the user, including:
   #- Press any key to continue when dialogue is done
  # - Use arrow keys to maneuver choice selection
   #- Use Enter to select a choice
   #- Select Inventory to open the inventory
#4. Displays the main menu options (Start, Options, Controls, Exit, Credits) and handles the user's choice accordingly, appending the selected function to the `menu_sys_list`.


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

#Exits the game by clearing the console screen and printing "Exiting Game" before calling the `exit()` function to terminate the program.


    os.system('clear')
    print("Exiting Game")
    exit()

def Credits():

#The `Credits()` function is responsible for displaying the credits for the game. It performs the following tasks:

#1. Clears the console screen using `os.system('clear')`.
#2. Prints the text "Created By:" and "Futuluhtoogan".
#3. Prompts the user to press Enter to continue.
#4. Prints the text "With the help of:" and "The Jittleyang Community".
#5. Prompts the user to press Enter twice.
#6. Prompts the user to enter whether they are a "Jittleyang or a Futuluhtoogan".
#7. Prints a blank line.
#8. Displays the main menu options (Start, Options, Controls, Exit, Credits) and handles the user's choice accordingly, appending the selected function to the `menu_sys_list`.


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

#The `main_movement()` function is responsible for managing the player's main movement options in the game. It performs the following tasks:

#1. Prints a blank line.
#2. Defines a list of choices for the player to select from: "Shop", "Dungeon", "Inn", "Main Menu", and "Inventory".
#3. Prompts the player to make a choice using the `menu()` function.
#4. Checks the player's choice:
   #- If the choice is 4 (Main Menu), it calls the `main_menu()` function.
   #- If the player has less than 5 actions remaining for the day, it checks the choice:
   #  - If the choice is 1 (Shop), it increments the player's actions by 1 and calls the `shop()` function.
   #  - If the choice is 2 (Dungeon), it increments the player's actions by 1 and calls the `dungeon()` function.
   #  - If the choice is 3 (Inn), it calls the `end_day()` function and prints "You have entered the inn".
   #  - If the choice is 5 (Inventory), it calls the `Inventory()` function.
   #- If the player has 5 actions remaining for the day, it checks the choice:
    # - If the choice is 3 (Inn), it calls the `end_day()` function and prints "You have entered the inn".
    # - Otherwise, it prints "You Have run out of actions for the day please rest at the inn" and calls the `main_movement()` function.


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

    #Displays the player's inventory, allows the player to use items, and updates the player's health and gold accordingly.
    
    #This function is responsible for managing the player's inventory. It first prints out all the items the player currently has in their inventory. It then prompts the player to choose whether they would like to use any items. If the player chooses to use an item, the function allows them to select which item to use from the list of items in their inventory. The function then updates the player's health and removes the used item from the inventory.
    
    #If the player chooses not to use any items, the function returns to the main movement menu.
    
    os.system('clear')
    print(" You Have the Follwing items")
    for thing in new_player.inventory:
        print(thing)
    print("\n")
   
    print("You have " + str(new_player.gold) + " gold")
    print("You have " + str(new_player.health) + " health")
    print("Would you like to use any items? ")
    choice = menu(["Yes", "No"])
    if choice == 1:
        print("What would you like to use? ")
        new_player.inventory.append("")
        
        choice = menu(new_player.inventory)
        
        if choice == 1:
            
            new_player.health =  new_player.health + new_player.inventory[choice - 1].healing 
            new_player.inventory.remove(new_player.inventory[choice -1])
            
       
    else:
        main_movement()

def dungeon():

#Handles the main dungeon gameplay loop. Generates a random set of enemies, displays their stats, and enters a combat loop with the player. If the player reaches the 10th floor, they are prompted to play a game of Wordle to win the game.


    from wordle import playworlde
    import random
    from Characters import enemy
    os.system('clear')
    floor = 1
    
    enemy_list = []
    goblin = enemy("Globin", random.randint(5,20), random.randint(1,10), random.randint(5,50))

    enemy_list.append(goblin)
    enemy_list.append(goblin)
    enemy_list.append(goblin)
    enemy_first_0 = random.choice(enemy_list)
    print("You encounter a " + enemy_first_0.name)
    print(" It has " + str(enemy_first_0.health) + " Health, " + str(enemy_first_0.attack_DMG) + " AD " + str(enemy_first_0.attack_PW) + " AP")
    
    if floor == 10:
        print("You have reached the top floor of the dungeon solve this to win the game")
        playworlde()
        
    else:
        print("You have " + str(new_player.health) + " health")
        print("You have " + str(new_player.gold) + " gold")
        print("You are on the " + str(floor) + " floor")
        fight(enemy_first_0,floor)


def fight(enemy_first,floor):

#Handles the main combat loop of the dungeon gameplay. Displays the enemy's stats, and enters a combat loop with the player. If the player reaches the 10th floor, they are prompted to play a game of Wordle to win the game.

#Args:
    #enemy_first (enemy): The first enemy encountered in the dungeon.
    #floor (int): The current floor of the dungeon.

#Returns:
    #None


    from Characters import enemy
    print("\n")
    if enemy_first.health <= 0:
        floor = floor + 1
        print("You have defeated the " + enemy_first.name)
        new_player.gold += (enemy_first.attack_DMG * enemy_first.attack_PW * random.choice([.8, 1.2, .5 ,.4]))
        print("You have " + str(new_player.gold) + " gold")
        print("You have " + str(new_player.health) + " health")
        
        choice = menu(["Continue", "Leave"])
        if choice == 1:
            dungeon()
        elif choice == 2:
            main_movement()

    elif new_player.health <= 0:
        print("You have died")
        exit()

    elif new_player.health >= 0 and enemy_first.health >= 0:   
        choice = menu(["Attack", "Defend", "Flee", "Inventory"])
        

        
        if choice == 1:
            enemy_first.health -= (new_player.AD + new_player.AP * 1.5)
            print("You have attacked the " + enemy_first.name)
            print("It has " + str(enemy_first.health) + " Health")
            enemy_first.attack(new_player)
            print("You have " + str(new_player.health) + " Health")
            fight(enemy_first,floor)
        elif choice == 2:
            new_player.health -= enemy_first.attack_DMG * .25
            print("You have defended against the " + enemy_first.name)
            print("It has " + str(enemy_first.health) + " Health")
            enemy_first.attack(new_player)
            print("You have " + str(new_player.health) + " Health")
            fight(enemy_first,floor)

        elif choice == 3:
            print("You Attempt to Flee " + enemy_first.name)
            random.randint(1,10)
            

            if random.randint(1,10) > 5:
                print("You have escaped from the " + enemy_first.name)
                main_movement()
            else:
                print("Flee Failed")
                print("You have " + str(new_player.health) + " Health")
                enemy_first.attack(new_player)
                fight(enemy_first,floor)
        elif choice == 4:
            Inventory()

        else:
            fight(enemy_first,floor)
   


