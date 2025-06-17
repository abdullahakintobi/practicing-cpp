def linear_search(array, target):
    for result in range(len(array)):
        if array[result] == target:
            return result
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
  result = linear_search(array, target)
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


