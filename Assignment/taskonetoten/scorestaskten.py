sum = 0
counter = 0

for count in range (10):
	score = float(input('Enter Score: '))

	if score >= 0 and score <= 100:
		counter += 1
		sum += score

print(f"The average of the valid scores  is {sum/counter}")