sum = 0

for count in range (10):
	score = float(input('Enter Score: '))

	if score >= 0 and score <= 100:
		sum += score

print(f"The sum of the valid scores  is {sum}")