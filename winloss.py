from Player  import game_player
import menusys


def check():

#Checks the player's status and determines if they have lost the game.

#If the player's actions are 0, it checks if the player's health is less than or equal to 0, or if the player's gold is less than or equal to 0. If either of these conditions is true, it prints a message indicating that the player has lost the game and exits the program.

#If the player's actions are not 0, it calls the `check()` function recursively.


    print("running check")
    if menusys.new_player.actions == 0:
        if menusys.new_player.health <= 0:
            print("You have lost, You died.")
            exit()
        elif menusys.new_player.gold <= 0:
            print("You have lost, You ran out of gold and got exiled from the village.")
            exit()
        else:
            check()