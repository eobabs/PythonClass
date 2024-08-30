'''
PSEUDOCODE

1. Request a number of choice from the user.
2. Set a recurrent multiplication from 1 to 10 with the inputted number.
3. Print result 

'''

number_of_choice = int(input("Enter number of your choice: "))
for count in range (1,11):
	multiple_of_number_inputted = count * number_of_choice
	print (number_of_choice, " × ", count , "  = ", multiple_of_number_inputted)