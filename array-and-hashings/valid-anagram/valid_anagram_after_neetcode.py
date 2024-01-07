# Given two strings s and t, return true if t is an anagram of s, and
# false otherwise.  An Anagram is a word or phrase formed by
# rearranging the letters of a different word or phrase, typically
# using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


# for better time complexity
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT


# for better space complexity


def is_anagram2(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


x = "anagram"
y = "nagaram"
print(is_anagram(x, y))

x = "rat"
y = "car"
print(is_anagram(x, y))

# From my understanding my way may be slightly better because with this
# current implementation, the function iterates through both strings
# in their entirety, then compares the dictionaries to one another,
# returning True or False if they are identical.

# My way iterates through string 's' and creates a hashmap of its
# characters and their count. Then, iterates through 't' to check if
# the characters of 't' are in the 's' hashmap. If it comes across a
# letter that is not in 's' or the count of each characters is not 0,
# it will return False. If not returns True. It's only "better" because
# there is a chance of NOT having to iterate through all of 't' based on
# luck.


# Method 1:
# Time Complexity: O(n)
# Memory Complexity:O(n)

# Method 2:
# Time Complexity: O(n log n)
# Memory Complexity: O(1) - O(n)
