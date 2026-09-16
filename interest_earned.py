# Matthew Cires 
#CMP 131
#Lab -01
#Week 4 
#9/11/26
#interest_earned.py
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate: "))
times= int(input("  Enter the number of compounding periods: "))
rate = rate /100
amount = principal *(1 + rate / times) ** times 
interest = amount - principal
print("Interest earned report")
print()
print("-----------------------")
print("Principal amount: $", format(principal, ".2f"))
print("Annual interest rate:" , format(rate*100, ".2f") , "%")
print("Compounding_periods:", times)
print()
print("Final account balance: $", format(amount, ".2f"))
print("interest earned: $", format(interest, ".2f"))
