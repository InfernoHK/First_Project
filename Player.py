class game_player:
    def __init__(self, name, health, inventory, AP, AD, gold):
        print("*He's right, what is my name?*")
        self.name = input("What is Your Name You Have Chosen Citizen? ")
        self.health = health
        self.inventory = inventory
        self.AP = AP
        self.AD = AD
        self.gold = gold
        self.day = 1
        self.actions = 0
        
        
        

       