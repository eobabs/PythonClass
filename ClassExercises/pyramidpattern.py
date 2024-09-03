pyramid_number = int(input("Enter a number: "))

for number in range (1, pyramid_number + 1):
	print()
	for counter in range (number, 0):
		
		space = " "
		print (space * (pyramid_number - number), number, end = " ")


help(max)