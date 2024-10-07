import random

count_correct = 0
for count in range (10):

	number_one = random.randrange(100)
	number_two = random.randrange(100)
	
	if number_one > number_two :
		result = number_one - number_two
		print(f"What is the difference? {number_one} - {number_two}")

	if number_two > number_one :
		result = number_two - number_one
		print(f"What is the difference?  {number_two} - {number_one} ")
		
	user_choice = int(input("Enter the difference: "))

	if user_choice == result :
		count_correct += 1

print (f"You have completed the exercise and scored {count_correct}/10")

