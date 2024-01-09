# Given an array of integers nums and an integer target, return indices
# of the two numbers such that they add up to target.You may assume
# that each input would have exactly one solution, and you may not use
# the same element twice. You can return the answer in any order.


def two_sum(nums, target):
    nums_table = {}
    # Use a dictionary to optimize search.

    for index, num in enumerate(nums):
        # iterate through each element
        comp = target - num
        # calculate what key we are going to look for.
        if comp in nums_table:
            # checks if key is in dictionary
            return [index, nums_table[comp]]
            # If found, returns that key's value and the current index as a list

        nums_table[num] = index
        # If not found adds a key, the current elements value during iteration, with
        # the value of the index of the current place in the iteration.


x = [2, 7, 11, 15]
y = 9
print(two_sum(x, y))
# [0,1]

x = [3, 2, 4]
y = 6
print(two_sum(x, y))
# [1,2]

x = [3, 3]
y = 6
print(two_sum(x, y))
# [0,1]

# Time Complexity: O(n)
# Space Complexity: O(n)
