class Bank:
    custId = 0
    name = "john doe"
    opening_bal = 0
    current_bal = 0

    def __init__(self):
        print("hello from init")

    def setData(self, id, n, ob):
        self.custId = id
        self.name = n
        self.opening_bal = self.current_bal = ob

    def display(dft):
        print(f"welcome {dft.name}, your current balance is {dft.current_bal}")

obja = Bank()
objb = Bank()
obja.setData(456800, "ironman", 1500)
objb.setData(456798, "thor", 1800)

#obja.display()
