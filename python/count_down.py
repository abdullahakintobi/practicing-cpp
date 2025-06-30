def count_down(num):
    if num == 0:
        print("Lift off!")
    else:
        print(num)
        count_down(num - 1)

# Test Case
print(count_down(5))
      
'''
Output:
5
4
3
2
1
Lift off!
None
'''
