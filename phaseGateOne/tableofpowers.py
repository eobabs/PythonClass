
MINIMUM_BASE_NUMBER = 1
MAXIMUM_BASE_NUMBER = 5

print ("base", "%4s" % 'power', "%4s" %  'result', '\n', end='  ')

for base in range (MINIMUM_BASE_NUMBER, MAXIMUM_BASE_NUMBER + 1):
	power = base + 1
	result = base**power

	print (base, "%3s" % "", power, "%3s" % "", result, '\n', end='  '  )
	

