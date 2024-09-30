import random

first_number = random.randrange(0, 100)
second_number = random.randrange(0,100)

sum_of_numbers = first_number + second_number


print(f"What is the sum {first_number} and {second_number}?")

user_input =int(input('Enter your answer: '))

if user_input == sum_of_numbers: 
	print ("True")
else: 
	print ("False")



