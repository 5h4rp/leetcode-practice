# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

from functools import reduce

l = list(map(int, input().split()))


def productExceptSelf(nums):
    pref_prod = [1]
    for i in range(len(nums)):
        pref_prod.append(pref_prod[i]*nums[i])
    print(pref_prod)

    suff_prod = [1]
    for i in range(len(nums)):
        suff_prod.insert(0, suff_prod[-i-1]*nums[-i-1])
    print(suff_prod)

    answer = []
    for i in range(len(nums)):
        answer.append(pref_prod[i] * suff_prod[i+1])

    return answer


print(productExceptSelf(l))
