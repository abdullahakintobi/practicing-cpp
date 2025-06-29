# Implement factorial calculation using recursion
def factorial(num):
    if num == 1:
        return num
    else:
        return (num * factorial(num-1))
        
# Test case
nums = [1, 2, 5, 8, 10, 13, 16]

for num in nums:
    print(f"The factorial of {num} is {factorial(num)}")
    
    
'''
Output:
The factorial of 1 is 1
The factorial of 2 is 2
The factorial of 5 is 120
The factorial of 8 is 40320
The factorial of 10 is 3628800
The factorial of 13 is 6227020800
The factorial of 16 is 20922789888000
'''
