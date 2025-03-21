class Basket:
    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.items = []

    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})
        self.data_manager.basket = self.items
        self.data_manager.save_basket()

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            self.items.pop(index)
            self.data_manager.basket = self.items
            self.data_manager.save_basket()

    def to_dict(self):
        return self.items