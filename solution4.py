# Write code for algorithm 4 below

def power(a, b):
    # base case
    if b == 0:
        return (1)
    
    #recursive case
    else:
        return a * power(a, b - 1)

print(power(2, 4))