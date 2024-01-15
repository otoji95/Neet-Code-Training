# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
import heapq


def top_k_frequent(nums, k):
    nums_hashmap = (
        {}
    )  # Initialize a dictionary to keep track of each number and its frequency.
    for num in nums:  # Iterate over each number
        if num not in nums_hashmap:  # If the number is not a key in our nums_hashmap
            nums_hashmap[num] = 1  # add the num as the key and begin its count at 1
        else:  # If it is found
            nums_hashmap[num] += 1  # increase its count by 1.

    heap = (
        []
    )  # Initialize a heap to keep track of the tuples of numbers with their count.
    for (
        num,
        freq,
    ) in nums_hashmap.items():  # Deconstructs each freq/num pair from the hashmap.
        heapq.heappush(heap, (freq, num))  # Push each of our tuples of freq/num pairs
        if len(heap) > k:  # If the length of our heap is larger than k
            heapq.heappop(
                heap
            )  # Pop off the tuple with the lowest value in the [0] index
    result = (
        []
    )  # Initialize a list to hold the nums with the highest counts. Length based on k

    while heap:  # While heap still has elements
        freq, num = heapq.heappop(heap)  # Pops off and deconstructs lowest counted
        result.append(num)  # Appends the number from the original array to results
    return result  # Returns the results array


nums = [1, 1, 1, 2, 2, 3]
print(top_k_frequent(nums, 2))

nums = [3, 0, 1, 0]
print(top_k_frequent(nums, 1))

# Time Complexity: O(n + k log k)

# Space Complexity: O(n + k)
