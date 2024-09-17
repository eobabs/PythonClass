def small_pattern(number):
	for counter in range(number, 0, -1) :
		print ()
		for count in range (counter, 0, -1):
			print (count, end = ' ')


small_pattern(13)