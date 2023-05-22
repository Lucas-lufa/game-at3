from player import Player
from user_interface import User_Interface
import math

print(math.sqrt(9))

player_input = ""

player = Player()
is_alive = True

while is_alive == False or player_input != "quit":
    
    player_input = input()
    if player_input == 'dead':
        is_alive = False