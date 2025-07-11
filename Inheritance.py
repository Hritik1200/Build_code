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

class Credit_limit(Creditc2):
    def All_info():
        print("Total Credit Limit ",Limit1 +Limit2)

a = Credit_limit
a.info()
a.bank_AC()
a.card1(4000)
a.card2(4000)
a.All_info()


# using input method
class customer:
    def info(id,n):
        print("Customer ID :",id,"Customer Name: ",n)

class Bank(customer):
    def bank_AC(card_type,card_number):
        print("Card Type:",card_type,"Card Number:",card_number)

class Creditc1(Bank):
    def card1(tran1,limit1,tran2,limit2):
        global Limit1
        Limit1 = limit1
        global Limit2
        Limit2 = limit2
        print("Transaction ID:",tran1," Amount:",limit1)
        print("Transaction ID:",tran2,"Amount:",limit2)

class Bank1(Creditc1):
    def bank_AC1(card_type1,card_number1,tran3,limit3):
        global Limit3
        Limit3 = limit3
        print("Card Type:",card_type1,"Card Number:",card_number1)
        print("Transaction ID:",tran3,"Amount:",limit3)

class Credit_limit(Bank1):
    def All_info():
        print("Total Transaction Amount:",Limit1+Limit2+Limit3)

a = Credit_limit
a.info(input("Customer id"),input("Enter name"))
a.bank_AC(input("Enter card type"),input("Enter card No"))
a.card1(input("Enter Transaction ID1:"),int(input("enter limit1")),input("Enter Transaction ID2:"),int(input("enter limit2")))
a.bank_AC1(input("Enter card type"),input("Enter card No"),input("Enter Transaction ID3:"),int(input("enter limit3")))
a.All_info()

