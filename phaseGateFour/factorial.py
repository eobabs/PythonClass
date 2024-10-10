def factorial(number):

	product = 1 
	counter = 1

	while (counter <= number):
		product *= counter
		counter += 1


	return product


print(factorial(5))

