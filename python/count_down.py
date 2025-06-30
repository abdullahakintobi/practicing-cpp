# Count down using recursion
def count_down_recursion(num):
    if num == 0:
        print("Lift off!")
    else:
        print(num)
        count_down_recursion(num - 1)

# Count down using for loop
def count_down_for(num):
    for i in reversed((range(1, num + 1))):
        print(i)
    print("Lift off!")

# Count down using while loop
def count_down_while(num):
    while num > 0:
        print(num)
        num -= 1
    print("Lift off!")
