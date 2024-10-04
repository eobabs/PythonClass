checker = []

for numbers in range (1000, 3001, 2):		

	unit_digit = numbers % 10
	tens_digit = (numbers // 10) % 10
	hundreds_digit = (numbers // 100) % 10
	thousands_digit = (numbers // 1000)

	if (unit_digit % 2 == 0 and tens_digit % 2 == 0 and hundreds_digit % 2 == 0 and thousands_digit % 2 == 0 ):
		
		checker.append(numbers)
print(checker)



			
	
			
	