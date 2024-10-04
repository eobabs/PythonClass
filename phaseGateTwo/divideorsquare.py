import math

def divide_or_square(number):
    
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number.")
    
    if number < 0:
        raise ValueError("Invalid. Enter a positive number")

    if number % 5 == 0:
        return round(math.sqrt(number), 2)
    else:
        return number % 5




print(divide_or_square("abc"))

