from array_and_hashings.contains_duplicates.contains_duplicates_after_neetcode import (
    contains_duplicates,
)
from memory_profiler import memory_usage
import time


def test_empty_list():
    assert contains_duplicates([]) == False


def test_single_element():
    assert contains_duplicates([1]) == False


def test_large_list_no_duplicates():
    nums = list(range(10000))
    assert contains_duplicates(nums) == False


def test_worst_case_no_dupes():
    nums = list(range(9999))
    nums.append(9999)
    nums.append(10000)

    # Time Profiling
    start_time = time.time()
    result = contains_duplicates(nums)
    end_time = time.time()
    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"\n\n Approximate time: {elapsed_time_ms:.2f} ms")

    # Memory Profiling
    mem_usage = memory_usage((contains_duplicates, (nums,)))
    print(f"\nPeak memory usage: {max(mem_usage):.2f} MiB \n")

    assert result == False
