'''Suppose you want to deposit a certain amount of money into a savings account with a fixed annual interest rate. 
What amount do you need to deposit in order to have $XXXX in the account after XX years?'''

# Data needed
finalAccountValue = float(input("Enter final account value: "))
annualInterestRate = float(input("Enter the annual interest rate: "))
numberOfYears = float(input("Enter the number of years: "))

# main
annualInterestRate = annualInterestRate/100
initialDepositAmount = finalAccountValue/((1+annualInterestRate)**numberOfYears)

# Print
print("The initial value is:", initialDepositAmount)
