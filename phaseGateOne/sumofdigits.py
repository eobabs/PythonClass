"""
PSEUDOCODE
STEP 1: Prompt user to enter an integer between 0 and 1000 aand store in a variable integer_input
STEP 2: Check to see if user's input is within the boundaries of 0 and 1000 (The two numbers inclusive). If not tell user. Invalid Input.
STEP 3: If check is successful, assign the user's input to another variable to use for calculations
STEP 4: Initialize the sum of the digits to 0 to aid addition
STEP 5: Repeatedly extract each digit of the number and sum the extracted numbers together
STEP 6: Print result

"""

integer_input = int(input("Enter the integer between 0 and 1000: "))


if integer_input >= 0 and integer_input <= 1000:
	number = integer_input

	sum_of_digits = 0
	while (number != 0) :
		extracted_digit = number % 10
		sum_of_digits = sum_of_digits + extracted_digit
		number //= 10
	print(f"The sum of all the digits of {integer_input} is {sum_of_digits} ")

else :
	print("Invalid Input")