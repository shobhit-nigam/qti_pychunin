class Lunch:
    def __init__(self, dish, quantity):
        self.dish = dish
        self.quantity = quantity

    def heat(self):
        print(f"heating {self.dish}")

item_a = Lunch('roti', 2)
print(item_a.__dict__)
