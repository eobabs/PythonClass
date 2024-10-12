import random

lucky_number = random.sample(range(101), 3)

guess = input("Enter three numbers separated by spaces: ")
guess_list = guess.split()

guess_list = [int(numbers) for numbers in guess_list]

print("You predicted:", guess_list)
print("Winning numbers:", lucky_number)

if len(guess_list) != 3:
	print("Please enter exactly three numbers.")
else:
	if lucky_number == guess_list:
        	print("You have won 5000")
	elif sorted(lucky_number) == sorted(guess_list):
        	print("You have won 4000")
	elif (lucky_number[0] in guess_list and lucky_number[1] in guess_list) or (lucky_number[0] in guess_list and lucky_number[2] in guess_list) or (lucky_number[1] in guess_list and lucky_number[2] in guess_list):
        	print("You have won 3000")
	elif (guess_list[0] in lucky_number) or (guess_list[1] in lucky_number) or (guess_list[2] in lucky_number):
        	print("You have won 2000")
	else:
        	print("You have won NOTHING")
