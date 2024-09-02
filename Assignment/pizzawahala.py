"""
PSEUDOCODE


"""


pizza_type = input("Enter your preferred pizza type: ").strip().lower()
number_of_guests = int(input("Enter the number of expected guests: "))

if pizza_type == "Sapa Size" and number_of_guests > 0 :
	if number_of_guests % 4 == 0:
		orders_processed = number_of_guests // 4
		leftovers = (orders_processed * 4) - number_of_guests;
		print("Hello Customer\nYou have ", orders_processed, " boxes of ", pizza_type, " and it costs $", orders_processed * 2000);
		print("\nAlso, you will have ", leftovers, " slice(s) left after serving your guests.")
	else :
		orders_processed = number_of_guests // 4
		leftovers = ((orders_processed + 1) * 4) - number_of_guests;
		print("Hello Customer\nYou have ", orders_processed + 1, " boxes of ", pizza_type, " and it costs $", (orders_processed + 1) * 2000);
		print("\nAlso, you will have ", leftovers, " slice(s) left after serving your guests.")

elif pizza_type == "Small Money" and number_of_guests > 0 :
	if number_of_guests % 6 == 0:
		orders_processed = number_of_guests // 6
		leftovers = (orders_processed * 6) - number_of_guests;
		print("Hello Customer\nYou have ", orders_processed, " boxes of ", pizza_type, " and it costs $", orders_processed * 2400);
		print("\nAlso, you will have ", leftovers, " slice(s) left after serving your guests.")
	else :
		orders_processed = number_of_guests // 6
		leftovers = ((orders_processed + 1) * 6) - number_of_guests;
		print("Hello Customer\nYou have ", orders_processed + 1, " boxes of ", pizza_type, " and it costs $", (orders_processed + 1) * 2400);
		print("\nAlso, you will have ", leftovers, " slice(s) left after serving your guests.")

elif pizza_type == "Big Boys" and number_of_guests > 0 :
	if number_of_guests % 8 == 0:
		orders_processed = number_of_guests // 8
		leftovers = (orders_processed * 8) - number_of_guests;
		print("Hello Customer\nYou have ", orders_processed, " boxes of ", pizza_type, " and it costs $", orders_processed * 3000);
		print("\nAlso, you will have ", leftovers, " slice(s) left after serving your guests.")
	else :
		orders_processed = number_of_guests // 8
		leftovers = ((orders_processed + 1) * 8) - number_of_guests;
		print("Hello Customer\nYou have ", orders_processed + 1, " boxes of ", pizza_type, " and it costs $", (orders_processed + 1) * 3000);
		print("\nAlso, you will have ", leftovers, " slice(s) left after serving your guests.")

elif pizza_type == "Odogwu" and number_of_guests > 0 :
	if number_of_guests % 12 == 0:
		orders_processed = number_of_guests // 12
		leftovers = (orders_processed * 12) - number_of_guests;
		print("Hello Customer\nYou have ", orders_processed, " boxes of ", pizza_type, " and it costs $", orders_processed * 4200);
		print("\nAlso, you will have ", leftovers, " slice(s) left after serving your guests.")
	else :
		orders_processed = number_of_guests // 12
		leftovers = ((orders_processed + 1) * 12) - number_of_guests;
		print("Hello Customer\nYou have ", orders_processed + 1, " boxes of ", pizza_type, " and it costs $", (orders_processed + 1) * 4200);
		print("\nAlso, you will have ", leftovers, " slice(s) left after serving your guests.")

else :
	print("Invalid Order")
