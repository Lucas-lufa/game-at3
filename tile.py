death = "death"
water = "water"
forrest = "forrest"
sand = "sand"
bridge = "bridge"

class Tile:
    """ THe base tile with all the attributes, descriptions added to make different terrain """
    def __init__(self, _deadly : bool, _traversable : bool) -> None:
        """ _deadly True will end the game, _traversable False will stop the player """
        self._deadly = _deadly
        self._traversable = _traversable
        self.items = []

class        