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

        self.player_position = 8

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
            d,d,d,d,d,d,d,
            d,w,s,f,f,f,d,
            d,w,s,f,f,f,d,
            d,w,s,f,f,f,d,
            d,w,w,b,w,w,d,
            d,w,s,f,f,f,d,
            d,d,d,d,d,d,d
        ]

    def navigation(self, user_input):
        """ moves north, south, east and west """
        if user_input == self.north:
            self.player_position -= 8
        if user_input == self.south:
            self.player_position += 8
        if user_input == self.east:
            self.player_position += 1
        if user_input == self.west:
            self.player_position -= 1
