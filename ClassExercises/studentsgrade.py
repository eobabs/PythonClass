number_of_students = int(input("Enter number of students: "))

sum = 0
for _ in range (number_of_students):
	score_of_students = float(input("Enter score of student: "))
	sum += score_of_students

average = sum/number_of_students

print("The average grade of the class is: ", round(average, 3))
