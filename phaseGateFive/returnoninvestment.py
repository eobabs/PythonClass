INTEREST_RATE = 0.1

print("Year   Interest      Amount")

def get_ROI(amount, time):

	for year in range(1, time + 1):
		interest = INTEREST_RATE * amount
		new_amount = interest + amount
		amount = new_amount
		
		print(f"{year}      {interest:,.2f}     {new_amount:,.2f}")



get_ROI(1_000_000, 10)