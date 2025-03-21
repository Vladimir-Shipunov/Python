class Currency:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_dict(self):
        return {"название": self.name, "цена": self.price}