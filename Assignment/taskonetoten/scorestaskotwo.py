sum = 0

for count in range (10):
	score = float(input('Enter Score: '))
	sum += score

print(f"The average of the 10 scores is {sum/10}")