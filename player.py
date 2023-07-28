class Player:
    def __init__(self) -> None:
        self.is_alive = True
        self.hands = []

    def use(self):
        """ Takes out of hands or bag uses it.
        lists the items to chose from
        use selected item """
        pass

    def examine(self):
        """ Lists items or backpack.
        returns description of item """
        pass

    def put(self):
        """ Takes from bag and puts into items """
        pass

    def grab(self, thing):
        if len(self.hands) > 2:
            self.hands.append(thing)
        if len(self.hands) <= 2:
            print ("Hands are full!")