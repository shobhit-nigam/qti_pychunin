class Lunch:
    drink = 'buttermilk'
    def __init__(self, dish, quantity):
        self.dish = dish
        self.quantity = quantity

    def heat(self):
        print(f"heating {self.dish}")

item_a = Lunch('roti', 2)
item_b = Lunch('curry', '200 gms')
print(item_a.__dict__)
print(item_b.__dict__)

print("--------")
print(Lunch.__dict__)

print("--------")
print(vars(item_a))
