from array_and_hashings.contains_duplicates.contains_duplicates_after_neetcode import (
    contains_duplicates,
)
from memory_profiler import profile, memory_usage
import time


def test_empty_list():
    assert contains_duplicates([]) == False


def test_single_element():
    assert contains_duplicates([1]) == False


def test_large_list_no_duplicates():
    nums = list(range(10000))
    assert contains_duplicates(nums) == False


def test_large_list_with_duplicates_stats():
    nums = list(range(5000)) + list(range(5000))

    # Time profiling
    start_time = time.time()
    result = contains_duplicates(nums)
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000
    print(f"\n\nApproximate Time used: {elapsed_time:.2f} ms.")

    # Memory profiling
    mem_usage = memory_usage((contains_duplicates, (nums,)))
    print(f"\nPeak memory usage: {max(mem_usage):.2f} MB\n")

    assert result == True


def test_large_list_no_duplicates_stats():
    nums = list(range(10000))

    # Time profiling
    start_time = time.time()
    result = contains_duplicates(nums)
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000
    print(f"\n\nApproximate Time used: {elapsed_time:.2f} ms.")

    # Memory profiling
    mem_usage = memory_usage((contains_duplicates, (nums,)))
    print(f"\nPeak memory usage: {max(mem_usage):.2f} MB\n")

    assert result == False
