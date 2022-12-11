"""
Day 3 - Rucksack Reorganization

Our main challenge today is to efficiently find overlaps between groups. Since
ordering does not matter (that is "abcd" and "dbac" would be equivalent) we can
make use of Python's builtin `set` type. Like mathematical sets, `set` does not
store order but in return can efficiently compute overlaps (`.intersection`)
as well as other set relations such as unions.
"""
from typing import Any, Iterator
import io
import string


# We need the priority aka score of each letter a lot, so it helps to precompute them.
# This code is mainly long because of the speaking variable names; it could easily be
# compressed a little.
PRIORITY = {
    letter: priority for priority, letter in enumerate(string.ascii_lowercase, start=1)
} | {
    letter: priority for priority, letter in enumerate(string.ascii_uppercase, start=27)
}


def sum_duplicates(data: Iterator[str]) -> int:
    """Compute the priority sum of duplicates per line"""
    total = 0
    for items in data:
        # To get the left and right part of each line, we use *slicing*, which
        # generalises indexing. Instead of fetching by index as `...[index]`
        # we can fetch a sequence as `...[start:stop]`.
        # After computing the middle index `items[:middle]` and `items[middle:]`
        # are the left and right half of the sequence.
        middle = len(items) // 2
        # Mind the comma on the left side of the assignment. Assigning to a sequence
        # of names automatically unpacks an iterable from the right side.
        # Assigning to a sequence of a single name is a neat trick to get a single
        # item that ends up in an iterable (like a set).
        duplicate, = set(items[:middle]).intersection(items[middle:])
        total += PRIORITY[duplicate]
    return total


def sum_groups(data: Iterator[str]) -> int:
    """Compute the priority sum of duplicates per group"""
    total = 0
    # The `zip` builtin merges multiple iterables; `zip([0, 1, …], ["a", "b", …])`
    # gives us `(0, "a"), (1, "b"), …`. By using it on three slice, each providing
    # every third item but from a different start, we get the first three,
    # the next three, … items at once.
    # A more efficient version of this is defined in day6, using generators.
    for a, b, c in zip(data[::3], data[1::3], data[2::3]):
        badge, = set(a).intersection(b).intersection(c)
        total += PRIORITY[badge]
    return total


def solve(data: io.StringIO) -> tuple[Any, Any]:
    data_buffer = [line.strip() for line in data]
    return sum_duplicates(data_buffer), sum_groups(data_buffer)
