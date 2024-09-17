def is_palindrome(number):
	str_number = str(number)
	return str_number == str_number[::-1]

def is_prime(number):
    if number <= 1:
        return False
    count = 0
    for checker in range(1, number + 1):
        if number % checker == 0:
            count += 1
    return count == 2


def is_palindrome_and_prime(number):
    if is_palindrome(number) and is_prime(number):
        return True
    return False



print(is_palindrome_and_prime(11))

