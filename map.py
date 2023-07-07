import tile 

class Map:
    """ Makes the map """
    def __init__(self) -> None:
        #test
        # self.keys = {
        #     "w": self.north,
        #     "south": "s",
        #     "T": None 
        # }
        ##

        self.north = "w"
        self.east = "d"
        self.south = "s"
        self.west = "a"

        self.death = tile.Death()
        self.water = tile.Water()
        self.forrest = tile.Forrest()
        self.sand = tile.Sand()
        self.bridge = tile.Bridge()

        d = self.death
        w = self.water
        f = self.forrest
        s = self.sand
        b = self.bridge
        
        """ Need to generate map """
        self.map_tiles = [
            [d,d,d,d,d,d,d],
            [d,w,s,f,f,f,d],
            [d,w,s,f,f,f,d],
            [d,w,s,f,f,f,d],
            [d,w,w,b,w,w,d],
            [d,w,s,f,f,f,d],
            [d,d,d,d,d,d,d]
        ]

        self.MAP_SIZE = len(self.map_tiles)
        self.x_player_position = 1
        self.y_player_position = 1

    @property
    def north_look(self):
        return self.x_player_position - 1
        
    @property
    def east_look(self):
        return self.y_player_position + 1
        
    @property
    def south_look(self):
        return self.x_player_position + 1
    
    @property
    def west_look(self):
        return self.y_player_position - 1
    
    def tile_string(self, x_position, y_position):
        """  """
        return self.map_tiles[x_position][y_position].__str__()

    def keep_in_bounds(self, coordinate, MAP_SIZE):
        if coordinate > MAP_SIZE :
            return coordinate -1
        if coordinate < 0 :
            return coordinate +1
        return coordinate
        """ stops going out side of the bounds of the map """
        player_position = position - 1
        if len(self.map_tiles) -1 <= player_position or player_position < 0:
            return position
        else:
            return player_position

    def navigation(self, user_input):
        """ moves north, south, east and west """
        if user_input == self.north:
            self.x_player_position = self.keep_in_bounds(self.north_look,self.MAP_SIZE)
        if user_input == self.south:
            self.x_player_position = self.keep_in_bounds(self.south_look,self.MAP_SIZE)
        if user_input == self.east:
            self.y_player_position = self.keep_in_bounds(self.east_look,self.MAP_SIZE) 
        if user_input == self.west:
            self.y_player_position = self.keep_in_bounds(self.west_look,self.MAP_SIZE)
