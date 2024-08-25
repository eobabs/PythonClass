"""
PSEUDOCODE

1. Request for 3 inputs from user and store them in three different variables
2. Multiply the duration inputted by 12 and store as a variable (to get the duration in months)
3. Divide the rate inputted by 1200 to get monthly rate in decimal and store as a variable
4. Add 1 to the new rate and raise the result to the power of the duration in months and store as a variable
5. Multiply the principal by the monthly rate and the result of step 4
6. Subtract 1 from your result in step 4
7. Use the result in step 6 to divide the result of step 5
8. Store it as a variable
9. Print result

"""
print ("")

principal = float(input("Enter the principal amount: "))
annual_rate = float(input("Enter the annual interest rate: "))
duration = float(input("Enter the duration of mortgage in years: "))

print ("")


time_in_months = duration * 12
monthly_percentage_rate = annual_rate/1200
new_rate = 1 + monthly_percentage_rate
rate_over_the_duration = new_rate**time_in_months

mortgage_value = (principal * monthly_percentage_rate * rate_over_the_duration) /( rate_over_the_duration - 1)

print("Your monthly payment is $", round(mortgage_value, 2))

print ("")
