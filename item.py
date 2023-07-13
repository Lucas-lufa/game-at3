class Item:
    def __init__(self, name: str, takeable: bool) -> None:
        self.name = name
        # if False item to large to take but can be seen from a distance
        self._takeable = takeable

    def __lt__(self, other):
        return self.name < other.name
    
class Tree(Item):
    def __init__(self, name = "Tree, ", takeable = False) -> None:
        super().__init__(name=name, takeable=takeable)
        self.description = "a tall eucalyptus. "
        self.branches = []

    def __str__(self) -> str:
        return self.name + self.description
    
class Rock(Item):
    def __init__(self, name = "Rock, " , takeable = True) -> None:
        super().__init__(name=name, takeable=takeable)
        self.description = "of a good size. "

    def __str__(self) -> str:
        return self.name
    
    def examine(self):
        return self.name + self.description
    
    def throw(self, index):
        int(index)
    
class Letter(Item):
    def __init__(self, letter_to: str, letter_message: str, letter_from: str,name = "Letter, ", takeable = True) -> None:
        super().__init__(name=name, takeable=takeable)
        self.letter_to = letter_to
        self.letter_message = letter_message
        self.letter_from = letter_from
        self.description = f"To {self.letter_to}, From {self.letter_from}. "

    def __str__(self) -> str:
        return self.name + self.description

    def letter_open(self):
        return self.letter_message

"""    item template
class (Item):
    def __init__(self, name = ", " , takeable = ) -> None:
        super().__init__(name=name, takeable=takeable)
        self.description = ". "

    def __str__(self) -> str:
        return self.name + self.description
"""