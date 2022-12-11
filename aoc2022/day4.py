from typing import Any, Iterator
import io


Pair = tuple[int, int, int, int]


def parse_pair(pair: str) -> Pair:
    return tuple(
        int(border)
        for task_range in
        pair.split(",")
        for border in
        task_range.split("-")
    )


def count_contains(pairs: Iterator[Pair]) -> int:
    total = 0
    for left_low, left_high, right_low, right_high in pairs:
        if left_low == right_low or left_high == right_high:
            total += 1
        elif left_low < right_low:
            if right_high < left_high:
                total += 1
        else:
            if right_high > left_high:
                total += 1
    return total


def count_overlap(pairs: Iterator[Pair]) -> int:
    total = 0
    for left_low, left_high, right_low, right_high in pairs:
        if left_low == right_low or left_high == right_high:
            total += 1
        elif left_low < right_low:
            if left_high >= right_low:
                total += 1
        else:
            if right_high >= left_low:
                total += 1
    return total


def solve(data: io.StringIO) -> tuple[Any, Any]:
    pairs = [parse_pair(line.strip()) for line in data]
    return count_contains(pairs), count_overlap(pairs)
