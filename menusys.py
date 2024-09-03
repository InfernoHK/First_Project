menu_sys = []

def main_menu():
    while menu_sys == []:
        menu_sys.append(main_menu)
        choices = (["Start","Options", "Controls","Exit", "Credits"])
        if choices() == 1:
            menu_sys.append(start)
            Start()
            break
        elif choices() == 2:
            menu_sys.append(Options)
            Options()
            break
        elif choices() == 3:
            menu_sys.append(Controls)
            Controls()
            break
        elif choices() == 4:
            menu_sys.append(Exit)
            Exit()
            break
        elif choices() == 5:
            menu_sys.append(Credits)
            Credits()
            break
    choices = ["Continue","Options", "Controls","Exit", "Credits"]


      
def Start ():
    print("")

def Options():
    print("No Options Currently Available")

def Controls():
    print("No Controls Or Keybind Remapping Currently Available")
    print("Press Any Key to Continue When Dialouge is Done")
    print("Arrow Keys to Maneuver Choice Selection")
    print("Enter to Select Choice")
    print("Type Inventory when in game to view your inventory")

def Exit():
    print("Exiting Game")
    exit()

def Credits():
    print("Created By:")
    print ("Futuluhtoogan")
    pause = input()
    print("With the heelp of:")
    print("The Jittleyang Community")
    pause = input()
    pause = input()
    team = input("Are you a Jittleyang or a Futuluhtoogan? ")
def main_movement():
    choices = ["Shop", "Dungeon", "Inn", "Main Menu"]
    if menu(choices) == 1:
        shop()