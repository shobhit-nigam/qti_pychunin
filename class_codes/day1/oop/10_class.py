class Bank:
    custId = 0
    name = "john doe"
    opening_bal = 0
    current_bal = 0

    def display(dft):
        print(f"welcome {dft.name}, your current balance is {dft.current_bal}")

obja = Bank()
objb = Bank()

obja.display()
# obja.display() --> Bank.display(obja)

objb.display()
# objb.display() --> Bank.display(objb)

objb.name = "naruto"
obja.rank = 5

print(obja.rank)
# error
print(objb.rank)
