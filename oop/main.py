class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_items(self, name, price):
        self.items.append({"name": name, "price": price})

    def stock_price(self):
        total = sum([i["price"] for i in self.items])
        print([i["price"] for i in self.items])
        return total


store_a = Store("123")
store_a.add_items("test", 123)
store_a.add_items("test", 123)
store_a.add_items("test", 123)
print(store_a.items)
print(store_a.stock_price())
