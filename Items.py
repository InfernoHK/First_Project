class Item:

#Represents an item in the game.

#Attributes:
    #name (str): The name of the item.
    #AD (int): The attack damage of the item.
   # AP (int): The ability power of the item.
    #sell_price (int): The price the item can be sold for.
    #healing (int): The amount of healing the item provides.


    def __init__(self, name, AD, AP, sell_price, healing):
        self.name = name
        self.AD = AD
        self.AP = AP
        self.sell_price = sell_price
        self.healing = healing
        

    