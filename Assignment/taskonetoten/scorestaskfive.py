sum = 0

for count in range (1,11):
	score = float(input('Enter Score: '))

	if score % 2 == 0:
		sum += score

print(f"The sum of the scores that are even number is {sum}")