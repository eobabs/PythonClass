sum = 0

for count in range (1,11):
	score = float(input('Enter Score: '))

	if count % 2 == 0:
		sum += score

print(f"The sum of the even index scores is {sum}")