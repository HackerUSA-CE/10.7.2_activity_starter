# Write code for algorithm 2 below

def natural_numbers(x,i):
	# base case
	if i > x:
		return 
	
    # recursive case
	else:
		print(i)
		return (natural_numbers( x, i + 1))

natural_numbers(3, 1)


# expected output: 1 2 3