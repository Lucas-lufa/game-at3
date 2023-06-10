from player import Player
from user_interface import User_Interface
from map import Map

# import math
# print(math.sqrt(9))

world_map = Map()
ui = User_Interface()
player_input = ""

player = Player()
is_alive = True

def string_to_cut(MAP_SIZE, x_player_position, y_player_position):
        """ Takes in a map size and player position
            gives back tile string or out of bounds string """
        if x_player_position < 0 or x_player_position >= MAP_SIZE:
            return "Look upon the void of reality"
        if y_player_position < 0 or y_player_position >= MAP_SIZE:
            return "Look upon the void of reality"
        return world_map.tile_string(x_player_position,y_player_position)

too_north = string_to_cut(world_map.MAP_SIZE,
                                    world_map.north_look,
                                    world_map.y_player_position)

too_west = string_to_cut(world_map.MAP_SIZE,
                                    world_map.x_player_position,
                                    world_map.west_look)

too_east = string_to_cut(world_map.MAP_SIZE,
                                    world_map.x_player_position,
                                    world_map.east_look)

too_south = string_to_cut(world_map.MAP_SIZE,
                                    world_map.south_look,
                                    world_map.y_player_position)

while player_input != "quit":
    p1,i1 = ui.cutup_string(10,
                     too_north,
                     80)
    print(p1)
    north = "\n" + " " * 40 + world_map.north
    print(north + f" x=  {world_map.x_player_position} y= {world_map.y_player_position}")
    p1, i1 = ui.cutup_string(10,
                        world_map.map_tiles
                            [world_map.x_player_position]
                            [world_map.y_player_position -1 ],
                        19)
    p2, i2 = ui.cutup_string(10,
                        world_map.map_tiles
                            [world_map.x_player_position]
                            [world_map.y_player_position],
                        38)
    p3, i3 = ui.cutup_string(10,
                        world_map.map_tiles
                            [world_map.x_player_position]
                            [world_map.y_player_position +1 ],
                        19)
    all_parts_print = "|"+p1+ world_map.west +p2+world_map.east+p3+"|"
    print(all_parts_print)
    south = " " * 40 + world_map.south + "\n"
    p1,i1 = ui.cutup_string(10,
                     world_map.map_tiles
                            [world_map.x_player_position +1 ]
                            [world_map.y_player_position],
                     80)
    print(south + p1)
    player_input = input()
    world_map.navigation(player_input)