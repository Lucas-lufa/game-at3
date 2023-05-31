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

        self.death = "death"
        self.water = "water"
        self.forrest = "forrest"
        self.sand = "sand"
        self.bridge = "bridge"

        d = self.death
        w = self.water
        f = self.forrest
        s = self.sand
        b = self.bridge
        
        self.map_tiles = [
            [d,d,d,d,d,d,d],
            [d,w,s,f,f,f,d],
            [d,w,s,f,f,f,d],
            [d,w,s,f,f,f,d],
            [d,w,w,b,w,w,d],
            [d,w,s,f,f,f,d],
            [d,d,d,d,d,d,d]
        ]

        self.player_position_x = 0
        self.player_position_y = 6

    def add_keep_in_bounds(self, position):
        """ stops going out side of the bounds of the map """
        player_position = position + 1
        if len(self.map_tiles) -1 <= player_position or player_position < 0:
            return position
        else:
            return player_position

    def minus_keep_in_bounds(self, position):
        """ stops going out side of the bounds of the map """
        player_position = position - 1
        if len(self.map_tiles) -1 <= player_position or player_position < 0:
            return position
        else:
            return player_position

    def navigation(self, user_input):
        """ moves north, south, east and west """
        if user_input == self.north:
            self.player_position_x = self.minus_keep_in_bounds(self.player_position_x)
        if user_input == self.south:
            self.player_position_x = self.add_keep_in_bounds(self.player_position_x)
        if user_input == self.east:
            self.player_position_y = self.add_keep_in_bounds(self.player_position_y) 
        if user_input == self.west:
            self.player_position_y = self.minus_keep_in_bounds(self.player_position_y)
