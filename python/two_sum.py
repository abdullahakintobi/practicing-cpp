# LeetCode: https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    num_map = {}  # Dictionary to store number and its index
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index

# Test Case
nums = [
    [2, 7, 11, 15],         # num1
    [-3, 4, 3, 90],         # num2
    [3, 2, 4, 7, 9],        # num3
    [3, 4, 7, 1, 8, 9, 6],  # num4
    ]
target = [9, 0, 11, 16]     # [target1, target2, target3, target4]

for i in range(len(target)):
    print(f"Test {i}: {twoSum(nums[i], target[i])}")  
    
    
'''
Output:
Test 0: [0, 1]
Test 1: [0, 2]
Test 2: [2, 3]
Test 3: [2, 5]
'''
