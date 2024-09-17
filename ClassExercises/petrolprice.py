'''
PSEUDOCODE

1. Request budget from user and store in a variable
2. Dvided budget by 855 and store in a variable
3. Print result
'''

budget = int(input('Enter your budget: $'))

PRICE_PER_LITER = 855

number_of_liters = budget/PRICE_PER_LITER

print(f"The number of litres to be bought is  {number_of_liters: .2f}")