''' PSEUDOCODE
Step 1 : Request for first input
Step 2 : Store user's input as number1
Step 3 : Request for second input
Step 4 : Store user's input as number2
Step 5 : Request for third input
Step 6 : Store user's input as number3
Step 7 : Calculate the sum of the three inputs
Step 8 : Store it as sum
Step 9 : Divide sum by 3
Step 10: Store it as average
Step 10 : Print the output
''' 

number1 =  int(input ("Enter the first number:"))
number2 =  int(input ("Enter the second number:"))
number3 =  int(input ("Enter the third number:"))

sum = number1 + number2 + number3
average = sum/3

print (" ")
print ("The average of the three numbers is ", round(average, 3))


