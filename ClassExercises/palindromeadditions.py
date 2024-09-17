number = int(input("Enter a number: "))

def palindromes_addition (number) :

	if number > 0 and number < 1000:
		if number < 10:
			return number		
		if number >= 10 and number < 100:
			unit_digit = number % 10
			tens_digit = number // 10
			if tens_digit % 2 == 0 and unit_digit % 2 == 0:
				sum = unit_digit + tens_digit
				return sum
			elif tens_digit % 2 == 1 and unit_digit % 2 == 1:
				difference = tens_digit - unit_digit
				return difference
			else :
				return "Nothing is done"
		if number >= 100 and number <= 999:
			unit_digit = number % 10
			tens_digit = (number // 10) % 10
			hundreds_digit = number // 100
			if tens_digit % 2 == 0 and unit_digit % 2 == 0:
				if hundreds_digit % 2 == 0:
					sum = unit_digit + tens_digit + hundreds_digit
					return sum
				else :
					return "Nothing is done"
			elif tens_digit % 2 == 1 and unit_digit % 2 == 1:
				if hundreds_digit % 2 == 1:
					difference = hundreds_digit - tens_digit - unit_digit
					return difference
				else :
					return "Nothing is done"
			else :
				return "Nothing is done"
	else :
		return "Invalid Input"

print (palindromes_addition (number))