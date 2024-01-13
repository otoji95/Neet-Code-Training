# Given an array of strings strs, group the anagrams together. You
# can return the answer in any order.  An Anagram is a word or phrase
# formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.


def group_anagrams(strs):
    res = {}  # initialize a dictionary to store

    for s in strs:  # Iterate over each string
        count = [
            0
        ] * 26  # Create an array with 26 zeros. One for each letter of the alphabet.

        for c in s:  # Iterate over each character in current string.
            count[ord(c) - ord("a")] += 1

        count_tuple = tuple(
            count
        )  # Convert count to a tuple, as lists are not hashable

        if count_tuple not in res:  # If count_tuple is not already a key in dict,
            res[count_tuple] = [s]  # Add it to a new list
        else:  # or if it is a key
            res[count_tuple].append(s)  # append it to existing list for this key.

    return list(res.values())  # return the values of dicts.


# Time Complexity: O(kn) k being length of string

# Space Complexity: O(kn)
