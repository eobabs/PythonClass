for number in range(1, 51):
	if number % 3 == 0:
		print("Fizz")
		if number % 5 == 0 and number % 3 == 0:
			print ("FizzBuzz")
	elif number % 5 == 0:
		print("Buzz")
	else:
		print (number)