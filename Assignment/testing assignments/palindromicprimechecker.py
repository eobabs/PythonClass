def is_palindrome(number):
	number_in_string = str(number)
	return str_number == number_in_string[::-1]

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

