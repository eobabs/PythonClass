
def get_maximum(first_number, second_number, third_number):

	largest_number = first_number


	if first_number == "" and second_number == "" and c == "":
		print ("invalid")

	if first_number > largest_number:
		largest_number = first_number
		
	if second_number > largest_number :
		largest_number = second_number
		
	if third_number > largest_number :
		largest_number = third_number
	return largest_number
	

print("The maximum number is ", get_maximum(-3,-4,-8))


def get_minimum(first_number, second_number, third_number):

	lowest_number = first_number


	if first_number == "" and second_number == "" and c == "":
		print ("invalid")

	if first_number < lowest_number:
		lowest_number = first_number
		
	if second_number < lowest_number :
		lowest_number = second_number
		
	if third_number < lowest_number :
		lowest_number = third_number
	return lowest_number
	

print("The minimum number is ",get_minimum(-3,-4,-8))
	