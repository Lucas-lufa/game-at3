class Item:
    def __init__(self, name: str, takeable: bool) -> None:
        self.name = name
        # if False item to large to take but can be seen from a distance
        self._takeable = takeable

    def __lt__(self, other):
        return self.name < other.name