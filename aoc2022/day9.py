from typing import Any, Iterator
import io
from functools import reduce


def draw(head: complex, tail: complex, start: complex):
    board = [["." for _ in range(6)] for _ in range(5)]
    for indicator, position in [("s", start), ("T", tail), ("H", head)]:
        board[int(position.imag)][int(position.real)] = indicator
    for line in reversed(board):
        print("".join(line))
    print()


def move_head(instructions: list[tuple[str, int]], start: complex = 0j) -> Iterator[complex]:
    steps = {"R": 1, "U": 1j, "L": -1, "D": -1j}
    position = start
    yield position
    for direction, amount in instructions:
        # print("==", direction, amount, "==")
        step = steps[direction]
        for _ in range(amount):
            position += step
            yield position


def follow_tail(head_positions: Iterator[complex], start: complex = 0j) -> Iterator[complex]:
    position = start
    for head in head_positions:
        delta = abs(position - head)
        print(position, "=?>", head, "by", delta)
        assert delta < 3, f"tail lost head: {delta=}"
        if delta < 2:
            pass
        elif delta == 2 or delta > 2.5:  # abs(2+2j) = 2.8284271247461903
            position += (head - position) / 2
        elif delta < 2.5:  # abs(1+2j) = 2.23606797749979
            position, old_position = head, position
            if abs(old_position.real - head.real) == 1:
                position -= 1j if head.imag > old_position.imag else -1j
            else:
                position -= 1 if head.real > old_position.real else -1
        # draw(head, position, start)
        assert abs(position - head) < 3, f"{position=}, {head=}"
        yield position


def solve(data: io.StringIO) -> tuple[Any, Any]:
    instructions = [
        (direction, int(amount)) for direction, amount in map(str.split, data)
    ]
    visited2 = set(follow_tail(move_head(instructions)))
    visited10 = set(
        reduce(lambda head, _: follow_tail(head), range(9), move_head(instructions))
    )
    return len(visited2), len(visited10)
