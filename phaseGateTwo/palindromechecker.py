def reverse(number):
	reversed_number = 0
	while(number != 0):
		reversed_number = (reversed_number * 10) + number % 10
		number //= 10

	return reversed_number

def is_palindrome(number):

	if number < 0 :
		return False
	
	if number == reverse(number):
		return True
	else:
		return False



print(is_palindrome(424))

print(is_palindrome(42004))
		 