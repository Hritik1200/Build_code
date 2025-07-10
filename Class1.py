
# Class: class means category which stores same category codes which can be used at same time if call class name

# 1. creating class using self method

class Bank:
    def Amount(self, amt):
        self.amt = amt  # we can change name varaible 
        print("Amount:", amt)

    def credit_amt(self, cre_amt):
        self.cre_amt1 = cre_amt  # we can change name varaible eg: self.cre_amt1
        print("Credit Limit:", cre_amt)

    def withdrawal(self, withd):
        self.withd = withd
        print("Withdrawal Amount:", withd)

    def aft_wid(self):
        total = (self.amt + self.cre_amt1) - self.withd
        print("Balance After Withdrawal:", total)


# to call object
bank1 = Bank()
bank1.Amount(5000)
bank1.credit_amt(2000)
bank1.withdrawal(1500)
bank1.aft_wid()


# 2. we can use any name other than self eg:
# in this mehod i have used name a as bridge

class Bank:
    def Amount1(a,amt1):
        a.amt2 = amt1
        print("Amount =",amt1)

    def cre_amt1(a,cre):
        a.cre2 = cre
        print("Credit Limit =",cre)

    def withdrawal1(a,with1):
        a.with2 = with1
        print("Withdrawal =",with1)

    def aft_wid1(a):
        Total1 = (a.amt2 + a.cre2)-a.with2
        print("Banlance After Withdrawal =",Total1)



# to call object

bank1 = Bank()
bank1.Amount1(5000)
bank1.cre_amt1(3000)
bank1.withdrawal1(1000)
bank1.aft_wid1()




# 3.creating class using global method

class Bank:
    def amount(amt):
        global Amount
        Amount = amt
        print("Amount :",amt)
    def credit_l(cre):
        global Credit1
        Credit1 = cre
        print("Credit Limit :",cre)
    def withdrawal(withd):
        global Withd1
        Withd1 = withd
        print("Withdrawal Amount :",withd)
    def aft_wid():
        total = (Amount + Credit1)-Withd1
        print("Balace After Withdrawal :",total)



# to call object
Bank()
Bank.amount(10000)
Bank.credit_l(5000)
Bank.withdrawal(2000)
Bank.aft_wid()
