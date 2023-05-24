class Map:
    def __init__(self, player):
        self.player = player
        self.tiles = [
            [Title("Fish", "W"), Title("Fish", "W"), Title("Fish", "W"), ],
            [Title("Fish", "W"), Title("Fish", "W"), Title("Fish", "W"), ],
            [Title("Fish", "W"), Title("Fish", "W"), Title("Fish", "W"), ]
        ]
    
    def show(self):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(y):
                if self.player.position[0] == x and self.player.position[1] == y:
                    print(self.player.char)
                    continue
                elif tile.entity is not None:
                    print(tile.entity.char)
                    continue
                print(tile.char)
    

class Player:
    def __init__(self):
        self.map = Map(self)
        self.position = (0, 0)
        self.char = 'o'
        self.inventory = []

    def move(self, x=0, y=0):
        self.position[0] += x
        self.position[1] += y
    
    def interact(self):
        item = self.map.titles[self.position[0]][self.position[1]].item
        if item is not None and item.is_intractable:
            self.pickup(item)
        print("I cant pick this up")

    def pickup(self, item):
        self.inventory.append(item)


class Game:
    def __init__(self) -> None:
        pass


class Item(ABC):
    def __init__(self, intractable: bool) -> None:
        self.is_intractable = intractable
    
    @abstractmethod
    def __str__(self):
        pass

class Weapon(Item):
    def __init__(self):
        super(Weapon, self).__init__()
    
    def __str__(self):
        return "This is a gun!"
    
    # def __call__(self):
    # pass
    
    

class Title:
    def __init__(self, item = None, char: str = '') -> None:
        self.char = char
        self.item = item
