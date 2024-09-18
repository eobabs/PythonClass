sum = 0
counter = 0

while (counter != 10):
	score = float(input('Enter Score: '))

	if score >= 0 and score <= 100:
		counter += 1
		sum += score

print(f"The sum of the scores that are even number is {sum}")