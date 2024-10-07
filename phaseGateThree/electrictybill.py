units_of_electricity = float(input("Enter number of units: "))


STANDARD_UNIT = 100


if units_of_electricity > 200:
	electricity_charge = (STANDARD_UNIT * 0) + (STANDARD_UNIT * 50) + (units_of_electricity - STANDARD_UNIT * 2) * 100
	print (f"You desire {units_of_electricity:.2f} units and the electricty charge is {electricity_charge:.2f}")

elif units_of_electricity > 100 and units_of_electricity <= 200:
	electricity_charge = (STANDARD_UNIT * 0) + (units_of_electricity - STANDARD_UNIT) * 50
	print (f"You desire {units_of_electricity:.2f} units and the electricty charge is {electricity_charge:.2f}")

elif units_of_electricity >= 0 and units_of_electricity <= 100:
	electricity_charge = (STANDARD_UNIT * 0) 
	print (f"You desire {units_of_electricity:.2f} units and the electricty charge is {electricity_charge:.2f}")

else:
	print("Invalid value entered.")


	