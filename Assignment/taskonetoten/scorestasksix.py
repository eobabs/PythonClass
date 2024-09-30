sum = 0
counter = 0

for count in range (1,11):
	score = float(input('Enter Score: '))

	if score % 2 == 0:
		counter += 1
		sum += score

print(f"The average of the scores that are even number is {sum/counter}")