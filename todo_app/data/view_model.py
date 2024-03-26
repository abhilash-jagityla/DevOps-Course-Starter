class ViewModel:
    def __init__(self, items: list[Items]):
        self._items = items
 
    def items(self):
        return self._items