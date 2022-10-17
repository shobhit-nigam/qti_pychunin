class Bank:

    def __init__(self, id, n, ob):
        self.custId = id
        self.name = n
        self.opening_bal = self.current_bal = ob

    def display(dft):
        print(f"welcome {dft.name}, your current balance is {dft.current_bal}")

obja = Bank(456800, "ironman", 1500)
objb = Bank(456798, "thor", 1800)

obja.display()
