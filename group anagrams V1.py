# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.


from collections import Counter

l = input('enter space seperated list of words: ').split()


def resCheck(s, res):

    if len(res) == 0:
        res.append([s])
    else:
        i = 0
        while i < len(res):

            if len(s) == len(res[i][0]) and Counter(s) == Counter(res[i][0]):
                res[i].append(s)
                break
            else:
                if (i + 1) == len(res):
                    res.append([s])
                    break
                i += 1


def groupAnagrams(strs):
    res = []

    for i in strs:
        resCheck(i, res)

    return res


print(groupAnagrams(l))

# eat tea tan ate nat bat
