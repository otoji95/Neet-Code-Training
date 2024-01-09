# Given an integer array nums, return true if any value appears at
# least twice in the array, and return false if every element is
# distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


def contains_duplicates(nums) -> bool:
    hash_set = set()
    # creates set track each number

    for n in nums:
        # iterates through each number in nums
        if n in hash_set:
            # if it finds a number thats already in that set, returns True
            return True
        # if not in set adds number
        hash_set.add(n)

    # returns False if it makes it through the Array if there are no duplicates.
    return False


x = [1, 2, 3, 1]
print(contains_duplicates(x))
x = [1, 2, 3, 4]
print(contains_duplicates(x))
x = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(contains_duplicates(x))

# Time Complexity: O(1) - O(n)

# Space Complexity: O(1) - O(n)
