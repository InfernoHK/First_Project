
class game_player:

    #Represents a game player with various attributes such as name, health, inventory, action points (AP), attack damage (AD), and gold.
    
    #The player's name is set by prompting the user for input. Other attributes are initialized with the provided values.
    
    #Attributes:
        #name (str): The name of the player.
        #health (int): The current health of the player.
        #inventory (list): The items in the player's inventory.
        #AP (int): The action points available to the player.
        #AD (int): The attack damage of the player.
        #gold (int): The amount of gold the player has.
       # day (int): The current day in the game.
       # actions (int): The number of actions the player has performed.
    
        
    def __init__(self, name, health, inventory, AP, AD, gold):
        print("*He's right, what is my name?*")
        self.name = input("What is Your Name You Have Chosen Citizen? ")
        self.health = health
        self.inventory = []
        self.AP = AP
        self.AD = AD
        self.gold = gold
        self.day = 1
        self.actions = 0
        
        
        

       