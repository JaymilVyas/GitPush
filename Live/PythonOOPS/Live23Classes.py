class car:
    def __init__(self, body, engin, tyre):
        self.body = body
        self.engin = engin
        self.tyre = tyre

    def milage (self):
        print("milage of this car")

c = car("solid", "v6", "Radial")
print(c)

class tata(car):
    pass

t = tata("solid", "v8", "Radial1")
print(t)
print(t.milage())

class bank:
    def transaction(self):
        print("total transaction value")
    def account_opening(self):
        print("this will show you your account open status")
    def deposit(self):
        print("this will show your deposited amount")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("this will show you all the transaction happened to icici through hdfc")

class icici(HDFC_bank):
    pass

i=icici()
i.hdfc_to_icici()
i.deposit()
i.account_opening()
i.transaction()