import random

numbers = []

count = 0

sum_even_index = 0
sum_odd_index = 0
product = 1
sum = 0

for index in range (10):	
	numbers.append(random.randrange(50))
	count += 1
	sum += numbers[index]

	if index % 2 == 0 :
		sum_even_index += numbers[index]

	if index % 2 == 1:
		sum_odd_index += numbers[index]

	if index % 3 == 2:
		product *= numbers[index]

print(numbers)
print(f"The length of the list: {count}")
print(f"The sum of the elements in the even positions is: {sum_even_index} ")
print(f"The sum of the elements in the even positions is: {sum_odd_index} ")
print(f"The product of the elements in every third position is: {product} ")
print(f"The average of the elements in the list is: {sum / count} ")






			
	
			
	