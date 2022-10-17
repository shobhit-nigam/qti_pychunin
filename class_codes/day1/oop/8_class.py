class Bank:
    custId = 0
    name = "john doe"
    opening_bal = 0
    current_bal = 0

    def display(self):
        print(f"welcome {self.name}, your current balance is {self.current_bal}")

obja = Bank()
objb = Bank()

obja.display()
# obja.display() --> Bank.display(obja)

objb.display()
# objb.display() --> Bank.display(objb)

objb.name = "naruto"

objb.display()
