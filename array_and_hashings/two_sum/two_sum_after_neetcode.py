# Given an array of integers nums and an integer target, return indices
# of the two numbers such that they add up to target.You may assume
# that each input would have exactly one solution, and you may not use
# the same element twice. You can return the answer in any order.


def two_sum(nums, target):
    # same same
    prev_map = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i


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
