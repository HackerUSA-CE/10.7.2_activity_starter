# Write code for algorithm 1 below

# MY SOLUTION 
def do_math(n):
    #base case
    if n == 0:
        return (0)
    
    # recursive case
    else:
        print(n)
        return (do_math(n-1))

print(do_math(5))

# ACTIVITY SOLUTION
# def count_down(n):

#   #  Base case
#   if n==0:
#       return

#   #  Recursive case
#   else:
#       print(n)
#       count_down(n-1)

# # test case
# n=8
# count_down(n)