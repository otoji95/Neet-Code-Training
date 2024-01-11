from array_and_hashings.valid_anagram.valid_anagram_after_neetcode import is_anagram
from array_and_hashings.valid_anagram.valid_anagram_after_neetcode import is_anagram2
from memory_profiler import memory_usage, profile
import random
import string
import time


def test_anagram():
    string1 = "anagram"
    string2 = "nagaram"
    assert is_anagram(string1, string2) == True


def test_anagram2():
    string1 = "anagram"
    string2 = "nagaram"
    assert is_anagram2(string1, string2) == True


def test_not_anagram():
    string1 = "car"
    string2 = "rat"
    assert is_anagram(string1, string2) == False


def test_not_anagram2():
    string1 = "car"
    string2 = "rat"
    assert is_anagram2(string1, string2) == False


# Random string generator


def generate_string_and_reverse(size=10000):
    # Generate a random string of 'size' characters
    original_string = "".join(random.choices(string.ascii_letters, k=size)).lower()
    # Create the reverse of the original string
    reversed_string = original_string[::-1]

    return original_string, reversed_string


# Test with stats
def test_anagram_stats():
    original, reversed_str = generate_string_and_reverse()

    # Time profiling
    start_time = time.time()
    result = is_anagram(original, reversed_str)
    end_time = time.time()
    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"\n\nTime taken for anagram test: {elapsed_time_ms:.3f} ms")

    # Memory profiling
    mem_usage = memory_usage((is_anagram, (original, reversed_str)))
    print(f"\nPeak memory usage for anagram test: {max(mem_usage):.2f} MiB \n")

    assert result == True
