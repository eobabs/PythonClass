grade = int (input ('Enter your score:'))

result = "not valid"

if grade >= 90 and grade <= 100 :
	result = "You are one of the best"
elif grade >= 80 and grade < 90:
	result = "You got A+"
elif grade >= 70 and grade < 80:
	result = "You got A"
elif grade >= 60 and grade < 70:
	result = "You got B"
elif grade >= 50 and grade < 60:
	result = "You got C"
elif grade < 50:
	result = "You failed"
else :
	result

print (result)
