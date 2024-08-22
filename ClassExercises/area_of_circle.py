''' PSEUDOCODE
Step 1 : Input value for radius as 10
Step 2 : Store user's input as radius
Step 3 : Calculate radius * radius
Step 4 : Store as radius sqaure
Step 5 : Mulltiply radius square by 3.142
Step 6 : Store it as area of circle
Step 7 : Print the value of area
''' 

name = input ('Enter your name: ')
radius =  int(input ("Enter radius:"))
radius_square = radius**2
pi = 3.142
area = radius_square * pi
print ("The area of a circle with ", radius, "cm is", round(area,3))
print ('Thank you for using this application', name)

