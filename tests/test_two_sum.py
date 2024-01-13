from array_and_hashings.two_sum.two_sum_after_neetcode import two_sum
from memory_profiler import profile
import time


def test_two_sum_simple():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_repeating_elements():
    assert two_sum([3, 3], 6) == [0, 1]


@profile
def test_worst_case_with_stats():
    nums = range(10001)

    # Time Management
    start_time = time.time()
    result = two_sum(nums, 19999)
    end_time = time.time()

    elapsed_time_ms = (end_time - start_time) * 1000

    print(f"\n\nApproximate time: {elapsed_time_ms:.2f} ms")

    assert result == [9999, 10000]
