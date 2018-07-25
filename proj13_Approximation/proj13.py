# Name:
# Date:

# proj13: Credit Card Debt

class CreditCardDebt():

    # Problem 1: Paying the Minimum
    def __init__(self, outBalance, yrInterest, minPayment):
        self.outBalance = outBalance
        self.yrInterest = yrInterest
        self.minPayment = minPayment


class MinimumPay(CreditCardDebt):

    def __init__(self, outBalance, yrInterest, minPayment):
        self.outBalance = outBalance
        self.yrInterest = yrInterest
        self.minPayment = minPayment

    def minimumpay(self, outBalance, yrInterest, minPayment):
        Sum = 0
        Month = 1

        while Month != 13:
            currentBalan = self.outBalance
            minMonthpay = (float(self.minPayment) * float(currentBalan))
            interestPaid = ((float(self.yrInterest) / 12) * float(currentBalan))
            princiPaid = (float(minMonthpay) - float(interestPaid))
            remainBal = (float(currentBalan) - float(princiPaid))

            print
            print "Month:",Month
            print "Minimum monthly payment: $"+str(round(minMonthpay,2))
            print "Principle paid: $"+str(round(princiPaid,2))
            print "Remaining balance: $"+str(round(remainBal,2))
            Month = Month + 1
            Sum = Sum + minMonthpay
            currentBalan = remainBal

        print
        print "RESULT"
        print "Total amount paid: $"+str(round(Sum,2))
        print "Remaining balance: $"+str(round(remainBal, 2))

    # Problem 2: Paying Debt Off in a Year


class YearlyDebt(CreditCardDebt):
    def __init__(self, outBalance, yrInterest):
        self.outBalance = outBalance
        self.yrInterest = yrInterest

    def debtyear(self, outBalance, yrInterest):

        moInterestRt = (float(yrInterest) / 12)
        Variable = 10
        Counter = 1
        currentBal = outBalance

        while Counter != 13:
            updateBal = ((float(currentBal)) * (1 + float(moInterestRt)) - float(Variable))
            currentBal = updateBal
            Counter = Counter + 1

            if Counter == 12:
                if float(updateBal) > 0:
                    Variable = Variable + 10
                    Counter = 0
                    currentBal = outBalance
                if float(updateBal) <= 0:
                    break
            if float(updateBal) <= 0:
                break
        print
        print "RESULT"
        print "Monthly payment to pay off debt in 1 year: $" + str(Variable)
        print "Number of months needed: " + str(Counter)
        print "Balance: " + str(round(updateBal, 2))

    # Problem 3: Use bisection search to solve faster

class Bisectionsearch(CreditCardDebt):
    def __init__(self, outBalance, yrInterest):
        self.outBalance = outBalance
        self.yrInterest = yrInterest

    def bisectionsearch(self, outBalance, yrInterest):
        currentBal = outBalance

        moInterestRt = (float(yrInterest) / 12)

        lowerBound = (float(currentBal) / 12.0)
        upperBound = ((float(currentBal) * (1 + float(moInterestRt) ** 12.0)) / 12.0)

        month = 1

        remain = currentBal

        while remain >= 0.01:

            Payment = (upperBound + lowerBound) / 2
            print "hihi"
            while month < 13:
                newBal = float(currentBal) - float(Payment)
                moInter = float(moInterestRt)*float(newBal)
                remain = float(newBal)+float(moInter)
                print "heloo"

            if remain < 0.01:
                lowerBound = Payment
                remain = currentBal

            elif remain > 0.01:
                upperBound = Payment
                remain = currentBal
            month = month + 1
            print "freddie"

        print
        print "RESULT"
        print "Monthly payment to pay off debt in 1 year: $" + str(round(Payment,2))
        print "Number of months needed: "+ str(month)
        print "Balance: " + str(round(remain, 2))




# Starting bank service
print
print "Hello. Which bank service would you like today?"
Service = raw_input('''Enter '0' to calculate outstanding debt by paying the minimum. 
Enter '1' to calculate how to pay off debt in a year.
Enter '2' to test our newest feature Bisection Search: ''')
while True:
    if Service == "0":
        print
        print "Before we begin we will need information."
        outBalance = raw_input("Please enter the outstanding balance on your credit card: ")
        yrInterest = raw_input("Please enter the annual credit card interest rate as a decimal: ")
        minPayment = raw_input("Please enter the minimum monthly payment rate as a decimal: ")
        Bank = MinimumPay(outBalance,yrInterest,minPayment)
        Bank.minimumpay(outBalance, yrInterest, minPayment)
        break
    if Service == "1":
        print
        print "Before we begin we will need information."
        outBalance = raw_input("Please enter the outstanding balance on your credit card: ")
        yrInterest = raw_input("Please enter the annual credit card interest rate as a decimal: ")
        Bank = YearlyDebt(outBalance, yrInterest)
        Bank.debtyear(outBalance, yrInterest)
        break
    if Service == "2":
        print
        print "Before we begin we will need information."
        outBalance = raw_input("Please enter the outstanding balance on your credit card: ")
        yrInterest = raw_input("Please enter the annual credit card interest rate as a decimal: ")
        Bank = Bisectionsearch(outBalance, yrInterest)
        Bank.bisectionsearch(outBalance, yrInterest)