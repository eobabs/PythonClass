number = int(input("Enter your number to break at: "))

number_one = 0
number_two = 1
temp_number = 1

print (number_one, number_two, number_two, end =" ")

for check in range (number - 3):
	number_one = number_two
	number_two = temp_number
	temp_number = number_one + number_two

	print(temp_number, end =" ")

  