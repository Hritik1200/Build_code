# this is updated Credit Card Transaction System using Python Inheritance
# in this we can can call same function card1 multiple times to print Amount which will
# be added in total limit

class customer:
    def info(id,n):
        print("Customer ID :",id,"Customer Name: ",n)

class Bank(customer):
    def bank_AC(card_type,card_number):
        print("Card Type:",card_type,"Card Number:",card_number)
        
Limit1 = 0
class Creditc1(Bank):
    def card1(tran1,limit1):
        global Limit1
        Limit1 += limit1
        print("Transaction ID:",tran1," Amount:",limit1)

class Bank1(Creditc1):
    def bank_AC1(card_type1,card_number1):
        print("Card Type:",card_type1,"Card Number:",card_number1)

class Credit_limit(Bank1):
    def All_info():
        print("Total Transaction Amount:",Limit1)

# this method is to take user input
a = Credit_limit
a.info(input("Customer id"),input("Enter name"))
a.bank_AC(input("Enter card type"),input("Enter card No"))
a.card1(input("Enter Transaction ID1:"),int(input("enter limit1")))
a.bank_AC1(input("Enter card type"),input("Enter card No"))
a.All_info()

# we have to run this in different cell or every time we have to give all input
a.card1(input("Enter Transaction ID1:"),int(input("enter limit1")))
a.All_info()


# if we dont want to change value every time when we run code

a = Credit_limit
a.info(123,"Hritik")
a.bank_AC("Visa",880567840)
a.card1("T001",6000)
a.bank_AC1("Amex",7890456738)
a.All_info()

# this is how we can call card1 function multiple times

a.card1("T002",6000)
a.All_info()
a.card1("T003",68900)
a.All_info()

# Output

Customer ID : 123 Customer Name:  Hritik
Card Type: Visa Card Number: 880567840
Transaction ID: T001  Amount: 6000
Card Type: Amex Card Number: 7890456738
Total Transaction Amount: 6000
Transaction ID: T002  Amount: 6000
Total Transaction Amount: 12000
Transaction ID: T003  Amount: 68900
Total Transaction Amount: 80900



# Credit Card Transaction System using Python Inheritance

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






