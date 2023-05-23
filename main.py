from player import Player
from user_interface import User_Interface
from map import Map
import math

print(math.sqrt(9))
world_map = Map()
ui = User_Interface()
player_input = ""

player = Player()
is_alive = True


while player_input != "quit":   
    
    player_input = input()
    world_map.navigation(player_input)


