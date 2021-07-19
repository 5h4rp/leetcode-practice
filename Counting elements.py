# Given an integer array arr, count element x such that x + 1 is also in arr.

# If there're duplicates in arr, count them seperately.

# Examples:
# Input: arr = [1,3,2,3,5,0]
# Output: 3
# Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.

# Input: arr = [1,1,2]
# Output: 2
# Explanation: Two 1s are counted cause 2 is in arr.

from collections import Counter

l = list(map(int, input().split()))


def countElements(arr):
    c = Counter(arr)
    res = 0
    for i in c.keys():
        if (c[i+1] != 0):
            res = res + c[i]

    return res


print(countElements(l))
