# Given two strings s and t, return true if t is an anagram of s, and
# false otherwise.  An Anagram is a word or phrase formed by
# rearranging the letters of a different word or phrase, typically
# using all the original letters exactly once.


# for better time complexity
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    # Checks if length of each string are equal. If they are not, it returns False

    countS, countT = {}, {}
    # create two dictionaries, one for each string to track each characters count.

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    # Iterates through each character in the strings and adds their elements as
    # keys paired with their count as the value.

    return countS == countT
    # Iterates through each dictionary and checks to make sure that key and value pairs match.


# for better space complexity
def is_anagram2(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


# Method 1:
# Time Complexity: O(n)
# Memory Complexity:O(n)

# Method 2:
# Time Complexity: O(n log n)
# Memory Complexity: O(1) - O(n)
