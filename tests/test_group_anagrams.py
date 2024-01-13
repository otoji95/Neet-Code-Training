from array_and_hashings.group_anagram.group_anagrams_after_neetcode import (
    group_anagrams,
)
from memory_profiler import profile
import random
import string
import time


def test_group_anagram():
    output = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected_output = [
        ["ate", "eat", "tea"],
        ["bat"],
        ["nat", "tan"],
    ]

    # Sort the inner lists and the outer list
    sorted_output = sorted([sorted(group) for group in output])

    assert sorted_output == expected_output


def test_group_anagram_empty_str():
    assert group_anagrams([""]) == [[""]]


def generate_random_string(length=10000):
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))


@profile
def test_worst_case_with_stats():
    n = 10000
    k = 100

    random_strings = [generate_random_string(k) for _ in range(n)]

    # Time Management
    start_time = time.time()
    result = group_anagrams(random_strings)
    end_time = time.time()

    # Basic checks

    # Check that each group contains anagrams
    for group in result:
        sorted_group = ["".join(sorted(s)) for s in group]
        for i in range(1, len(sorted_group)):
            assert (
                sorted_group[i] == sorted_group[0]
            ), "All strings in a group should be anagrams"

    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"\n\nApproximate time: {elapsed_time_ms:.2f} ms")

    assert sum(len(group) for group in result) == len(
        random_strings
    ), "Total number of elements should be the same"
    assert isinstance(result, list), "Output should be a list"


# Run the test
test_worst_case_with_stats()
