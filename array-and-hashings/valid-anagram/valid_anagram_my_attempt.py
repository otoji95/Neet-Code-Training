# Given two strings s and t, return true if t is an anagram of s, and
# false otherwise.  An Anagram is a word or phrase formed by
# rearranging the letters of a different word or phrase, typically
# using all the original letters exactly once.


def is_anagram(s: str, t: str) -> bool:
    counter = {}
    # creates dictionary to track each letter of 's' and their respective count

    if len(s) != len(t):
        # checks if lengths are equal. If not returns False.
        return False

    for letter in s:
        # For each letter in s, adds it to the counter dictionary. If its already there increments the counter.
        counter[letter] = counter.get(letter, 0) + 1

    for letter in t:
        if letter not in counter or counter[letter] == 0:
            return False
        counter[letter] -= 1
    # For each letter in t, checks if dict has that letter as a key, if it does subtracts one,
    # if dictionary does not have that letter as a key or if it does but that keys value == 0, it returns False.

    return True
    # Else returns True


x = "anagram"
y = "nagaram"
print(is_anagram(x, y))
# True

x = "rat"
y = "car"
print(is_anagram(x, y))
# False

# Time complexity: O(1) - O(n)

# Space complexity: O(n)
