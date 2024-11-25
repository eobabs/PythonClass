number_list = list(range(1,16))
print(number_list)

duplicated_number_list = number_list * 2
print(duplicated_number_list)

number_list_returned =list(set(duplicated_number_list))
print(number_list_returned)

def add_third_number(numbers):

    total = 0
    for index in range(2, len(numbers), 3):
        if type(numbers[index] is not int ):
            raise TypeError("Invalid Type")
        total += numbers[index]

    return total

def add_border_number(numbers):
        if len(numbers) % 2 == 0:
            middle_number = (numbers[len(numbers)//2] + numbers[(len(numbers)//2)-1])/2
            first_number = numbers[0]
            last_number = numbers[-1]
            total = first_number + middle_number + last_number
            return total
        else:
            middle_number = numbers[len(numbers) // 2]
            first_number = numbers[0]
            last_number = numbers[-1]
            total = first_number + middle_number + last_number

            return total


#print(add_third_number(number_list))
print(add_border_number(number_list))