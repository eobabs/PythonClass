def get_power(number):
	if number < 0:
		raise ValueError("Invalid number")

	if number == "":
		raise TypeError("Invalid input")

	return number ** 4