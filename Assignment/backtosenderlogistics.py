"""

PSEUDOCODE

1. Define statutory amount of 5000 and store in a variable
2. Prompt user for number of orders and store in a variable
3. Specify conditions for calculating the wage
4. If the user enters a number between 70 and 100(all inclusive), multiply by 500 and add statutory amount
5. If the user enters a number between 60 and 69(all inclusive), multiply by 250 and add statutory amount
6. If the user enters a number between 50 and 59(all inclusive), multiply by 200 and add statutory amount
7. If the user enters a number less than, multiply by 200 and add statutory amount
8. Store the value gotten in either of steps 4, 5, 6 or 7. Store in a variable.
9. Print result

"""


def main():

	wages_of_riders()

def wages_of_riders():

	STATUTORY_PAYMENT = 5000
	
	number_of_orders = int (input ('Enter the number of fulfilled orders:'))

	if number_of_orders >= 70 and number_of_orders <= 100 :
		wage_per_day = STATUTORY_PAYMENT + (500 * number_of_orders)
		print("You made",number_of_orders,"succesful orders\nYour wage for today is $", wage_per_day)

	elif number_of_orders >= 60 and number_of_orders < 70:
		wage_per_day = STATUTORY_PAYMENT + (250 * number_of_orders)
		print("You made",number_of_orders,"succesful orders\nYour wage for today is $", wage_per_day)

	elif number_of_orders >= 50 and number_of_orders < 60:
		wage_per_day = STATUTORY_PAYMENT + (200 * number_of_orders)
		print("You made",number_of_orders,"succesful orders\nYour wage for today is $", wage_per_day)

	elif number_of_orders < 50 and number_of_orders >= 0:
		wage_per_day = STATUTORY_PAYMENT + (160 * number_of_orders)
		print("You made",number_of_orders,"succesful orders\nYour wage for today is $", wage_per_day)

	else :
		print("Invalid number of successful orders.\nEnter the correct number of fulfilled orders")

if __name__ == "__main__":
    main()