base = int(input("Enter largest number of character on a line")

for printer in range(1, base + 1):
	left_side = "*" * printer
	reversed_left_side = "*" * (base + 1 - printer)

	right_side_space = " " * (printer - 1) 
	left_side_space = " " * (base - printer)
    
	print(f"{left_side:<15} {reversed_left_side:<15} {right_side_space + reversed_left_side} {left_side_space + left_side}")
