# Name:
# Date:

# proj13: Credit Card Debt


# Problem 1: Paying the Minimum
 outBalance = raw_input("Enter the outstanding balance on your credit card: ")
 yrInterest = raw_input("Enter the annual credit card interest rate as a decimal: ")
 minPayment = raw_input("Enter the minimum monthly payment rate as a decimal: ")
 minMonthpay = int(minPayment)
 interestPaid = int(yrInterest)/(12*int(outBalance))
 princiPaid = int(minPayment) - int(interestPaid)
 remainBal = int(outBalance) - int(princiPaid)
# Problem 2: Paying Debt Off in a Year

# Problem 3: Use bisection search to solve faster