class Bank:

    def __init__(self, id, n, ob):
        self.custId = id
        self.name = n
        self.opening_bal = self.current_bal = ob

    def display(self ):
        print(f"welcome {self.name}, your current balance is {self.current_bal}")

    def deposit(self, amt):
        self.current_bal = self.current_bal + amt
        print(f"thank you {self.name}, your deposit is successfull")

    def withdraw(self, amt):
        if self.current_bal > amt:
            self.current_bal = self.current_bal - amt
            print(f"thank you {self.name}, your withdrawal is successfull")
        else:
            print(f"you do not have enough balance")

obja = Bank(456800, "ironman", 1500)
objb = Bank(456798, "thor", 1800)

obja.withdraw(1900)
print("-"*10)
obja.deposit(1500)
print("-"*10)
obja.withdraw(1900)
print("-"*10)
obja.display()
