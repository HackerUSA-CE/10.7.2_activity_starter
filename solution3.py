# Write code for algorithm 3 below

def find_fibonacci(num):
    # base case
    print("Num",num)
    if num <= 1:
        return num

    #recursive case 
    else:
        return (find_fibonacci(num - 1) + find_fibonacci(num - 2))
    
print(find_fibonacci(10))