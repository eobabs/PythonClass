for printer in range(1, 11):
	left_side = "*" * printer
	reversed_left_side = "*" * (11 - printer)

	right_side_space = " " * (printer - 1) 
	left_side_space = " " * (10 - printer)
    
	print(f"{left_side:<15} {reversed_left_side:<10} {right_side_space + reversed_left_side} {left_side_space + left_side}")
