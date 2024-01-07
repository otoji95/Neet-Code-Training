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


def is_anagram(s: str, t: str) -> bool:
    # First step is to check if lengths match. If they do not match, we return False.
    # The second step is to iterate through s, putting its characters into key value pairs.
    # Each key is the letters inside of s, the values being the count of each letter inside of s.
    # Third  step is to iterate through t to see if the letters inside of t are inside of s as well with the same count.
    # If those conditions are false we return False, otherwise True.
    counter = {}
    if len(s) != len(t):
        return False
    for letter in s:
        counter[letter] = counter.get(letter, 0) + 1
    for letter in t:
        if letter not in counter or counter[letter] == 0:
            return False
        counter[letter] -= 1
    return True


x = "anagram"
y = "nagaram"
print(is_anagram(x, y))

x = "rat"
y = "car"
print(is_anagram(x, y))

# Time complexity: O(1) - O(n)

# Space complexity: O(n)
