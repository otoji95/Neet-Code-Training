from array_and_hashings.contains_duplicates.contains_duplicates_after_neetcode import (
    contains_duplicates,
)
from memory_profiler import profile
import time


def test_empty_list():
    assert contains_duplicates([]) == False


def test_single_element():
    assert contains_duplicates([1]) == False


def test_large_list_no_duplicates():
    nums = list(range(10000))
    assert contains_duplicates(nums) == False


@profile
def test_worst_case_with_stats():
    nums = list(range(9999))
    nums.append(9999)
    nums.append(10000)

    # Time Profiling
    start_time = time.time()
    result = contains_duplicates(nums)
    end_time = time.time()
    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"\n\n Approximate time: {elapsed_time_ms:.2f} ms")

    assert result == False
