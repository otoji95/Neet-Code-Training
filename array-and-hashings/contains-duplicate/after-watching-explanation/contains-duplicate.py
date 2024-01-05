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


def containsDuplicates(nums) -> bool:
    hash_set = set()
    for n in nums:
        if n in hash_set:
            return True
        hash_set.add(n)
    return False


x = [1, 2, 3, 1]
print(containsDuplicates(x))
x = [1, 2, 3, 4]
print(containsDuplicates(x))
x = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(containsDuplicates(x))


# From my understanding this way is better because it has a chance
# of finding the duplicate while iterating through the array.

# NeetCode way

# Time Complexity
# Best case O(1)
# Worst case O(n)

# Space Complexity
# Best case O(1)
# Worst case O(n)


# My way
# Time complexity
# Always O(n)

# Space complexity
# Always O(n)
