integer_input = int(input("Enter the integer you want to sum its digits: "))


if integer_input > 0 and integer_input <= 1000:
	unit_digit = integer_input % 10
	tens_digit =  (integer_input // 10) % 10
	hundreds_digit = (integer_input // 100) % 10
	thousands_digit = (integer_input) // 1000
	sum_of_digits = unit_digit + tens_digit + hundreds_digit + thousands_digit
	print(f"The sum of all the digits of {integer_input} is {sum_of_digits} ")
else :
	print("Invalid Input")





		