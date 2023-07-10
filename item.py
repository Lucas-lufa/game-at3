class Item:
    def __init__(self, name: str, takeable: bool) -> None:
        self.name = name
        # if False item to large to take but can be seen from a distance
        self._takeable = takeable

    def __lt__(self, other):
        return self.name < other.name
    
class Rock(Item):
    def __init__(self, name = "rock" , takeable = True) -> None:
        super().__init__(name=name, takeable=takeable)
        self.description = "A good sized rock. "

    def __str__(self) -> str:
        return self.description
    
class Tree(Item):
    def __init__(self, name = "tree", takeable = False) -> None:
        super().__init__(name=name, takeable=takeable)
        self.description = "Tall eucalyptus tree. "

    def __str__(self) -> str:
        return self.description