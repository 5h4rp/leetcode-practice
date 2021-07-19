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


from collections import defaultdict

l = input().split()


def groupAnagrams(strs):
    temp = defaultdict(list)
    for i in strs:
        temp[str(sorted(i))].append(i)
    return list(temp.values())


print(groupAnagrams(l))
