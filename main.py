from player import Player
from user_interface import UserInterface
from map import Map

# import math
# print(math.sqrt(9))

world_map = Map()
ui = UserInterface()
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


while player_input != "quit":
    """ Game loop """
    scene = world_map.tile_string(world_map.x_player_position, 
                                  world_map.y_player_position)
    if world_map.map_tiles[world_map.x_player_position][world_map.y_player_position]._deadly:
         print("Player died!")
         break
    
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

    ui.user_interface_one(too_north)
    ui.user_interface_three(too_west,
                            scene, 
                            too_east)
    ui.user_interface_one(too_south)
    print(str(world_map.x_player_position),str(
        world_map.y_player_position))
    player_input = input()
    world_map.navigation(player_input)