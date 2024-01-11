# Given an array of strings strs, group the anagrams together. You
# can return the answer in any order.  An Anagram is a word or phrase
# formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.


def group_anagrams(strs):
    sorted_dict = {}
    # create dictionary to store values as key value pairs

    return_list = []

    for str in strs:
        sorted_str = "".join(sorted(str))
        sorted_join = "".join(sorted_str)
        x = sorted_dict.get(sorted_join, [])
        if x:
            sorted_dict[sorted_join].append(str)
        else:
            sorted_dict[sorted_join] = [str]
    # for each str, group each str with its sorted

    for key in sorted_dict:
        return_list.append(sorted_dict[key])
    # for each key in the dict, append it to a list for the return

    return return_list


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))
# [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = [""]
print(group_anagrams(strs))
# [[""]]

strs = ["a"]
print(group_anagrams(strs))
# [["a"]]


# Time Complexity: O(n * k log k)
# Space Complexity: O(kn)
