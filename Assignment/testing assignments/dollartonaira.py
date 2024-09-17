def get_naira(currency):
	EXCHANGE_RATE = 1550
	
	if not isinstance (currency, (int, float)):
		return "Invalid input. Enter a valid number"

	if currency < 0:
		raise ValueError("Invalid number")

	return currency * EXCHANGE_RATE