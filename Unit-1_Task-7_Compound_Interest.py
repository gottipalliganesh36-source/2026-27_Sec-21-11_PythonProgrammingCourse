initial_amount = int(input("Enter amount: "))
interest_value = float(input("Enter the interest value: "))
compound_years = int(input("Enter the compound years: "))
amount = initial_amount * (1 + interest_value / 100) ** compound_years
compound_interest = amount - initial_amount
print("Compound Interest =", compound_interest)
