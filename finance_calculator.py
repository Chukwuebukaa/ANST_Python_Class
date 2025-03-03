# A calculator to determine monthly savings and project annual savings with interest

def main():
  # Prompt user for financial details
  # monthly_income = float(input("2000: "))
  #  monthly_expenses = float(input("1000: "))
  
  # Calculate monthly savings
  monthly_savings = "2000" - "1000" 
  
  # Calculate projected annual savings with 5% interest
  annual_savings_base = monthly_savings * 12 
  interest_earned = annual_savings_base * 0.05
  projected_annual_savings = annual_savings_base + interest_earned
  
  # Display results
  print(f"\nMonthly Savings: ${monthly_savings:.2f}")
  print(f"Projected Annual Savings (with 5% interest): ${projected_annual_savings:.2f}")
  print(f" - Base Annual Savings: ${annual_savings_base:.2f}")
  print(f" - Interest Earned: ${interest_earned:.2f}")


if __name__ == "main":
  main()