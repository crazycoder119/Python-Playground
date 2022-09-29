# Collect the necessary inputs : principal(initial amount borrowed), apr(anual interest rate), years
# Calculate the monthly payment

def loan_calculator():
    print("This is monthly loan payment calculator .......")
    principal = float(input("Enter the loan amount : "))
    apr = float(input("Enter the anual interest rate : "))
    years = int(input("Amount of years : "))
    monthly_interest_rate = apr/1200
    months = years * 12
    monthly_payment = principal * monthly_interest_rate/(1-(1+monthly_interest_rate) ** (-months))
    return monthly_payment

print("You have to pay monthly : ", str(loan_calculator()))