def binary_search(array, target):
    lower = 0
    upper = len(array) - 1

    while lower <= upper:
        midpoint = (upper + lower) // 2
        if array[midpoint] == target:
            return midpoint
        elif array[midpoint] > target:
            upper = midpoint - 1
        else:
            lower = midpoint + 1
    return None 

def verify(result):
    if result is None:
        return "Target not found in array"
    else:
        return f"Target was found in array at index: {result}"

# Test case
array = [x for x in range(1, 1001)]
targets = [1000, 1, 368, 974, 1001, 2025]

for target in targets:
  result = binary_search(array, target)
  print(verify(result))


'''
Output:
Target was found in array at index: 999
Target was found in array at index: 0
Target was found in array at index: 367
Target was found in array at index: 973
Target not found in array
Target not found in array
'''
