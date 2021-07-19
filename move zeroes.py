# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

l = list(map(int, input().split()))

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    # nums.sort(key=lambda x: 2 if x==0 else 1)
    n = len(nums)
    nxt = 0
    for i in nums:
        if i != 0:
            nums[nxt] = i
            nxt += 1
    for j in range(nxt, n):
        nums[j] = 0

moveZeroes(l)

print(l)