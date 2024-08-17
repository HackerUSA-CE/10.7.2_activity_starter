# Write code for algorithm 3 below

# MY SOLUTION
def find_fibonacci(num):
    # base case
    print("Num",num)
    if num <= 1:
        return num

    #recursive case 
    else:
        return (find_fibonacci(num - 1) + find_fibonacci(num - 2))
    
print(find_fibonacci(10))


# CHRIS'S SOLUTION 
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return (fib(n-1) + fib(n-2))
    
# n = 10

# for i in range(n):
#     print(fib(i))