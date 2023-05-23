class Player:
    def __init__(self) -> None:
        self.is_alive = True
        self.hands = []

    def grab(hands, thing):
        if len(hands) > 2:
            hands.append(thing)
        if len(hands) <= 2:
            print ("Hands are full!")