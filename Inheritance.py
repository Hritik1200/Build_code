class customer:
    def info():
        print("Customer Name : Hritik")

class Bank(customer):
    def bank_AC():
        print("Acc No:1059209062")

class Creditc1(Bank):
    def card1(limit1):
        global Limit1
        Limit1 = limit1
        print("Credit card Name : HDFC =",limit1)

class Creditc2(Creditc1):
    def card2(limit2):
        global Limit2
        Limit2 = limit2
        print("Credit card Name : SBI =",limit2)

class Credit_limit(Creditc2,Creditc1):
    def All_info():
        print("Total Credit Limit ",Limit1 +Limit2)

a = Credit_limit
a.info()
a.bank_AC()
a.card1(4000)
a.card2(4000)
a.All_info()