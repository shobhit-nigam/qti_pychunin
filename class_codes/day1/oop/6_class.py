class Bank:
    custId = 0
    name = "john doe"
    opening_bal = 0
    current_bal = 0

    def display():
        print("hello world")
        # print(f"welcome {name}, your current balance is {current_bal}")

obja = Bank()
objb = Bank()

print(obja.custId)
print(objb.custId)
print("-"*10)
obja.custId = 34680
print(obja.custId)
print(objb.custId)
