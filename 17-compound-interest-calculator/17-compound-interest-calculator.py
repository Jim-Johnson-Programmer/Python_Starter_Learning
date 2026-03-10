# 17-compound-interest-calculator
# Compound Interest Calculator - Simple Version (No Functions/Classes)

print("=== Compound Interest Calculator ===")
print()

# Get user input for the calculation
print("Enter the following information:")
principal = float(input("Initial amount (principal): $"))
annual_rate = float(input("Annual interest rate (%): "))
years = float(input("Number of years: "))
compounds_per_year = int(input("How many times per year is interest compounded? "))

print("\n" + "="*50)

# Convert percentage to decimal
rate_decimal = annual_rate / 100

# Calculate compound interest using formula: A = P(1 + r/n)^(nt)
# Where: A = final amount, P = principal, r = annual rate, n = compounds per year, t = time
amount = principal * (1 + rate_decimal / compounds_per_year) ** (compounds_per_year * years)

# Calculate the interest earned
interest_earned = amount - principal

# Display results
print(f"\nCOMPOUND INTEREST CALCULATION RESULTS:")
print(f"{'='*40}")
print(f"Principal (initial amount):    ${principal:,.2f}")
print(f"Annual interest rate:         {annual_rate}%")
print(f"Time period:                  {years} years")
print(f"Compounding frequency:        {compounds_per_year} times per year")
print(f"{'='*40}")
print(f"Final amount:                 ${amount:,.2f}")
print(f"Interest earned:              ${interest_earned:,.2f}")
print(f"{'='*40}")

# Show some additional calculations
total_return_percentage = (interest_earned / principal) * 100
effective_annual_rate = ((amount / principal) ** (1/years) - 1) * 100

print(f"\nADDITIONAL INFORMATION:")
print(f"Total return:                 {total_return_percentage:.2f}%")
print(f"Effective annual rate:        {effective_annual_rate:.2f}%")

print(f"\nYour ${principal:,.2f} invested at {annual_rate}% for {years} years")
print(f"compounded {compounds_per_year} times per year will grow to ${amount:,.2f}")