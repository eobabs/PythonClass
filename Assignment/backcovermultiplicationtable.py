def print_multiplication_table(start=2, end=12):
    
    print("    ", end="")
    for number in range(start, end + 1):
        print(f"{number:4}", end="")
    print()  

 
    for number in range(1, 13):
        print(f"{number:2} ", end="")  
        for second_number in range(start, end + 1):
            print(f"{number * second_number:4}", end="")
        print()  


print_multiplication_table()
