class Player:
    def __init__(self) -> None:
        self.is_alive = True
        self.hands = []

    def use(self, item):
        """ Takes out of hands or bag uses it.
        lists the items to chose from
        use selected item """
        item.use()

    def examine(self, item):
        """ Lists items or backpack.
        returns description of item """
        return item.examine()

    def put(self):
        """ Takes from bag and puts into items """
        pass

    def grab(self, thing):
        if len(self.hands) > 2:
            self.hands.append(thing)
        if len(self.hands) <= 2:
            print ("Hands are full!")