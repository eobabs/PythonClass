MINIMUM = 1
MAXIMUM = 10

print("    ", end = "")
for count in range (MINIMUM, MAXIMUM + 1):
	print ("%4d" % count, end = "")
	for counter in range  (MINIMUM, MAXIMUM + 1):
		print("%4d" % (count * counter), end = "")
	print()