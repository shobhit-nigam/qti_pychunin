class Bank:

    def __init__(self, id, n, ob):
        self.custId = id
        self.name = n
        self.opening_bal = self.current_bal = ob
        return None

    def display(dft):
        print(f"welcome {dft.name}, your current balance is {dft.current_bal}")

obja = Bank(456800, "ironman", 1500)
objb = Bank(456798, "thor", 1800)

x = obja.__init__(456802, "ironman", 1800)

obja.display()

print("return value of __init__", x)
