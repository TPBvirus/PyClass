import math

InvestmentAmount = input("Enter Investment: ")
AnnualInterest = input("Enter Annual Interest: ")
Years = input("Approximate number of years the investment will be held: ")

AnnualInterest = float(AnnualInterest)/100

InterestAccrued =  math.pow( (1 + (AnnualInterest/12 ) ) , 12 )

futureInvestmentValue = float(InvestmentAmount) * InterestAccrued

print("Accumulated Value: %.2f" % futureInvestmentValue)
