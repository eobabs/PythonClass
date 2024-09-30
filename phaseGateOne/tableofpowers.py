"""
PESUDOCODE
STEP 1: Set the minimum and maximum base numbers
STEP 2: Set the header of the table **
STEP 3: Add 1 to the value of the base and store in a variable named power
STEP 4: Raise the base to the power of the variable called 
"""

MINIMUM_BASE_NUMBER = 1
MAXIMUM_BASE_NUMBER = 5

print ("Base", "%4s" % 'Power', "%4s" %  'Result', '\n', end='  ')

for base in range (MINIMUM_BASE_NUMBER, MAXIMUM_BASE_NUMBER + 1):
	power = base + 1
	result = base**power

	print (base, "%3s" % "", power, "%3s" % "", result, '\n', end='  '  )
	

