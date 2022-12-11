from typing import Any, Iterator
import io
import string


PRIORITY = {
    letter: priority for priority, letter in enumerate(string.ascii_lowercase, start=1)
} | {
    letter: priority for priority, letter in enumerate(string.ascii_uppercase, start=27)
}


def sum_duplicates(data: Iterator[str]) -> int:
    total = 0
    for items in data:
        middle = len(items) // 2
        duplicate, = set(items[:middle]).intersection(items[middle:])
        total += PRIORITY[duplicate]
    return total


def sum_groups(data: Iterator[str]) -> int:
    total = 0
    for a, b, c in zip(data[::3], data[1::3], data[2::3]):
        badge, = set(a).intersection(b).intersection(c)
        total += PRIORITY[badge]
    return total


def solve(data: io.StringIO) -> tuple[Any, Any]:
    data_buffer = [line.strip() for line in data]
    return sum_duplicates(data_buffer), sum_groups(data_buffer)
