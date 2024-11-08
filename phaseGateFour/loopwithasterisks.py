for count in range (7):
	print()
	for number in range(1, count + 1):
		if number % 2 == 0:
			print("*",end = ' ')
		
		if number % 2 == 1:
			print (number, end = ' ')
	



for count in range (6, 0, -1):
	print()
	for number_below in range (1 , count +1):
		if number_below % 2 == 0:
			print("*",end = ' ')
		
		if number_below % 2 == 1:
			print (number_below, end = ' ')		
	