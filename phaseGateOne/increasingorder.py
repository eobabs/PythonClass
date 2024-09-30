first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

if first_number > second_number and first_number > third_number :
	if second_number > third_number: 
		print (f"The numbers in increasing order are {third_number}, {second_number}, { first_number}")
	else:
		print (f"The numbers in increasing order are {second_number}, {third_number}, { first_number}")

	
if second_number > third_number and second_number > first_number :
	if first_number > third_number: 
		print (f"The numbers in increasing order are {third_number}, {first_number}, { second_number}")
	else: 
		print (f"The numbers in increasing order are {first_number}, {third_number}, {second_number}")

if third_number > first_number and third_number > second_number :
	if first_number >  second_number: 
		print (f"The numbers in increasing order are {second_number}, {first_number}, {third_number}")
	else: 
		print (f"The numbers in increasing order are {first_number}, {second_number}, {third_number}")

