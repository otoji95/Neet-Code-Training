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
    # First Step in my mind would be to turn the list of nums into a set.
    # since sets do not have repeatable numbers. Then to compare the
    # length of the set of nums vs the length of nums. If they are equal,
    # we return false. The not, we return true.
    return len(set(nums)) != len(nums)


x = [1, 2, 3, 1]
print(containsDuplicates(x))
x = [1, 2, 3, 4]
print(containsDuplicates(x))
x = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(containsDuplicates(x))

# Time complexity: O(n)

# Space complexity: O(n)
