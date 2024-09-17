pyramid_number = int(input("Enter a number: "))

space = ""
control = pyramid_number

for number in range (1, pyramid_number + 1):
	print (" " * control, end = "")
	for counter in range (number, 1 , -1):
		print (counter, end = "")
	for counter in range (1, number + 1):
		print (counter, end = "")
	control -= 1
	print()


