class Item:
    def __init__(self, id, name, status='To Do'):
        self.id = id
        self.name = name
        self.status = status
    
    @classmethod
    def from_trello_card(cls, card, card_list):
        return Item(card['id'], card['name'], list['name'])

    