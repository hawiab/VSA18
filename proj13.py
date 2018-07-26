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

        monthlyInterestRate = float(yrInterest) / 12

        minimum = float(outBalance) / 12
        maximum = (float(outBalance) * (1 + float(monthlyInterestRate)) ** 12) / 12.0

        guessMinimum = (minimum + maximum) / 2

        remain = float(outBalance)

        counter = 1

        precision = 0.01

        while (remain >= precision):

            guessMinimum = (minimum + maximum) / 2

            for i in range(1, 13):
                newBalance = remain - guessMinimum
                monthInterest = float(yrInterest) / 12 * newBalance
                remain = newBalance + monthInterest

                counter += 1
                if counter > 12:
                    break

            if (remain < 0):

                maximum = guessMinimum
                remain = float(outBalance)
                counter = 1

            elif (remain > precision):
                minimum = guessMinimum
                remain = float(outBalance)
                counter = 1

        print "Monthly payment to pay off debt in a year:",round((float(guessMinimum)), 2)
        print "Number of months needed: "+ str(counter)
        print "Balance:", round(float(remain),2)
        # annualInterestRate = self.yrInterest
        # balance = self.outBalance
        # monthlyInterestRate = float(annualInterestRate) / 12
        # lowerBound = float(balance) / 12
        # upperBound = (float(balance) * (1 + float(annualInterestRate) / 12) ** 12) / 12
        # originalBalance = float(balance)
        # lowestBalance = 0.01
        # counter = 0
        # while abs(float(balance)) > float(lowestBalance):
        #     balance = originalBalance
        #     payment = (upperBound - lowerBound) / 2 + lowerBound
        #     for month in range(12):
        #         balance -= payment
        #         balance *= 1 + monthlyInterestRate
        #     if balance > 0:
        #         lowerBound = payment
        #     else:
        #         upperBound = payment
        #     counter += 1
        # print
        # print "RESULT"
        # print "Monthly payment to pay off debt in 1 year: $"+str(round(payment,2))
        # print "Balance:", round(balance, 2)

# Starting bank service
print
print "Hello. Which bank service would you like today?"

while True:
    try:
        Service = raw_input('''Enter '0' to calculate outstanding debt by paying the minimum. 
Enter '1' to calculate how to pay off debt in a year.
Enter '2' to test our newest feature Bisection Search: ''')
        break
    except ValueError:
        print "Please enter a valid input."

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
        break