# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


l = list(map(int, input().split()))

print(sum(l))


def findMaxLength(nums):
    first_oc = {}
    first_oc[0] = 0
    answer = 0
    pref = 0
    n = len(nums)
    for i in range(n):
        pref += (1 if nums[i] == 1 else -1)
        if pref in first_oc:
            answer = max(answer, i + 1 - first_oc[pref])
        else:
            first_oc[pref] = i + 1
        print('first oc: ', first_oc)
        print('pref: ', pref)
        print('i: ', i)
        print('answer: ', answer)
        print('next iteration')
    return answer


print(findMaxLength(l))
