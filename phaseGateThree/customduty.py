
cost_of_car = float(input("Enter cost: "))


HIGHEST_PERCENTAGE = 0.2
SECOND_TIER_PERCENTAGE = 0.15
THIRD_TIER_PERCENTAGE = 0.1
LOWEST_PERCENTAGE = 0.05

if cost_of_car > 10_000_000:
	duty_charge = cost_of_car * HIGHEST_PERCENTAGE
	print (f"The car costs {cost_of_car:.2f} and the duty charge of the car is {duty_charge:.2f}")

elif cost_of_car > 5_000_000 and cost_of_car <= 10_000_000:
	duty_charge = cost_of_car * SECOND_TIER_PERCENTAGE
	print (f"The car costs {cost_of_car:.2f} and the duty charge of the car is {duty_charge:.2f}")

elif cost_of_car >= 2_500_000 and cost_of_car <= 5_000_000:
	duty_charge = cost_of_car * THIRD_TIER_PERCENTAGE
	print (f"The car costs {cost_of_car:.2f} and the duty charge of the car is {duty_charge:.2f}")

elif cost_of_car < 2_500_000 and cost_of_car >= 0 :
	duty_charge = cost_of_car * LOWEST_PERCENTAGE
	print (f"The car costs {cost_of_car:.2f} and the duty charge of the car is {duty_charge:.2f}")

else:
	print("Invalid amount entered.")
	