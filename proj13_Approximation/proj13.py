# Name:
# Date:

# proj13: Credit Card Debt


# Problem 1: Paying the Minimum
def minimumpay(outBalance, yrInterest, minPayment):
    Sum = 0
    Month = 1

    while Month != 13:
        minMonthpay = (float(minPayment) * float(outBalance))
        interestPaid = ((float(yrInterest) / 12) * float(outBalance))
        princiPaid = (float(minMonthpay) - float(interestPaid))
        remainBal = (float(outBalance) - float(princiPaid))

        print
        print "Month:",Month
        print "Minimum monthly payment: $"+str(round(minMonthpay,2))
        print "Principle paid: $"+str(round(princiPaid,2))
        print "Remaining balance: $"+str(round(remainBal,2))
        Month = Month + 1
        Sum = Sum + minMonthpay
        outBalance = remainBal

    print
    print "RESULT"
    print "Total amount paid: $"+str(round(Sum,2))
    print "Remaining balance: $"+str(round(remainBal, 2))

# Problem 2: Paying Debt Off in a Year
# def debtyear(outBalance, yrInterest):
#     monthPayYr = (float(outBalance) / 12)
#     moInterestRt = (float(yrInterest)/12)
#     updateBal = ((float(outBalance)) * (1 + float(moInterestRt)) - float(monthPayYr))
#     month = 0
#     sum = 0
#     while month != 13:
#         if (12*10) < outBalance:

    # print
    # print "RESULT"
    # print "Monthly payment to pay off debt in 1 year: " + str(round(monthPayYr,2))
    # print "Balance: "+ str(round(updateBal,2))
# Problem 3: Use bisection search to solve faster


print "Hello. Which bank service would you like today?"
Service = raw_input("Enter 0 to calculate outstanding debt by paying the minimum. Enter 1 to calculate how to pay off debt in a year: ")
while True:
    if Service == "0":
        print
        print "Before we begin we will need information."
        outBalance = raw_input("Please enter the outstanding balance on your credit card: ")
        yrInterest = raw_input("Please enter the annual credit card interest rate as a decimal: ")
        minPayment = raw_input("Please enter the minimum monthly payment rate as a decimal: ")
        minimumpay(outBalance,yrInterest,minPayment)
        break
    if Service == "1":
        print
        print "Before we begin we will need information."
        outBalance = raw_input("Please enter the outstanding balance on your credit card: ")
        yrInterest = raw_input("Please enter the annual credit card interest rate as a decimal: ")
        # debtyear(outBalance,yrInterest)
        # break