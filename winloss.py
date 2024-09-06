from Player  import game_player
import menusys


def check():
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