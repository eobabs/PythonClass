"""
PESUDOCODE
STEP 1: Set the minimum and maximum base numbers as 1 and 5 respectively.
**STEP 2: Set the header of the table 
STEP 3: Add 1 to the value of the base and store in a variable named power
STEP 4: Raise the base to the power of the variable called power and store it in a variable called result
STEP 5: Print out result in the required format.
"""

MINIMUM_BASE_NUMBER = 1
MAXIMUM_BASE_NUMBER = 5

print ("Base", "%9s" % 'Power', "%6s" %  'Result', '\n', end='   ')

for base in range (MINIMUM_BASE_NUMBER, MAXIMUM_BASE_NUMBER + 1):
	power = base + 1
	result = base**power

	print (base, "%3s" % "", power, "%3s" % "", result, '\n', end='   '  )
	

