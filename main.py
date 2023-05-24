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
    p1,i1 = ui.cutup_strings(10,
                     world_map.map_tiles[world_map.player_position-8],
                     80)
    print(p1)
    p1, i1 = ui.cutup_strings(10,
                        world_map.map_tiles[world_map.player_position-1],
                        19)
    p2, i2 = ui.cutup_strings(10,
                        world_map.map_tiles[world_map.player_position],
                        38)
    p3, i3 = ui.cutup_strings(10,
                        world_map.map_tiles[world_map.player_position+1],
                        19)
    all_parts_print = "|"+p1+"|"+p2+"|"+p3+"|"
    print(all_parts_print)
    p1,i1 = ui.cutup_strings(10,
                     world_map.map_tiles[world_map.player_position+8],
                     80)
    print(p1)
    player_input = input()
    world_map.navigation(player_input)