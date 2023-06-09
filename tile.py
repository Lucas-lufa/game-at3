death = "death"
water = "water"
forrest = "forrest"
sand = "sand"
bridge = "bridge"

class Tile:
    """ THe base tile with all the attributes, descriptions added to make different terrain """
    def __init__(self, _deadly:bool, _traversable:bool ) -> None:
        """ _deadly True will end the game, _traversable False will stop the player """
        self._deadly = _deadly
        self._traversable = _traversable
        self.items = []

class Death(Tile):
    """ If on this tile will end the the game """
    def __init__(self, _deadly=True, _traversable=True) -> None:
        super().__init__(_deadly=_deadly, _traversable=_traversable)

        self.message = "A Dangerous place! "

    def __str__(self) -> str:
        return self.message

class Water(Tile):
    """ Water can not be traversed """
    def __init__(self, _deadly=False, _traversable=False) -> None:
        super().__init__(_deadly=_deadly, _traversable=_traversable)

        self.message = "Lovely water but you can't swim!. "

    def __str__(self) -> str:
        return self.message

class Bridge(Tile):
    """ The bridge crosses water, it is closed until quests done """
    def __init__(self, _deadly=False, _traversable=False) -> None:
        super().__init__(_deadly=_deadly, _traversable=_traversable)
#         eyes = "open" if self.pixels[10] == self.BLANK else "closed"
            
    def __str__(self) -> str:
        if self._traversable:
            self.message = "Bridge across the water. "
        else:
            self.message = "Bridge is closed. "
        return self.message

class Forrest(Tile):
    """ Tree tile items can be found in the canopy, trunk or under the tree """
    def __init__(self, _deadly=False, _traversable=True) -> None:
        super().__init__(_deadly=_deadly, _traversable=_traversable)

        self.message = "Forrest area full of trees. "

    def __str__(self) -> str:
        return self.message

class Sand(Tile):
    """ The items rocks can be found here """
    def __init__(self, _deadly=False, _traversable=True) -> None:
        super().__init__(_deadly=_deadly, _traversable=_traversable)

        self.message = "Sandy patch not much around. "
    
    def __str__(self) -> str:
        return self.message
