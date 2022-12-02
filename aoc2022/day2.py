"""
Day 2 - Rock Paper Scissors

This is a challenge in handling the unwieldy, circular RPS rules (R < P < S < R …).
We could use `if`/`elif`/`else` blocks to handle each case explicitly,
but there is a shorter way using math:
The trick is that modular arithmetic (`%` operator) applied to a sequence
naturally "wraps around".

There isn't actually a lot to say about how the formulas are derived.
If you are having trouble understanding them, write down a table of
inputs and manually computed outputs.

Since there are only so many possible combinations – 9 for each ruleset –
we pre-compute all combinations once. Afterwards, all we need to do is
directly lookup the score for each move combination.
"""
from typing import Any, Iterator
import io


# ### Parsing
# map from symbol to moves as A: 1, B: 2, …, X: 1, Y: 2, …
# this is a dict comprehension, which allows us to
# directly build a dict from an iteration.
MOVE = {
    # Python allows us to assign to several names at once:
    # `a, b = 1, 2` assigns 1 to a and 2 to b.
    # We can do the same in the target of a for loop:
    # just as `for x in …` assigns each item to `x`,
    # `for a, b in …` unpacks each item into `a` and `b`.
    symbol: move for move, symbol in (
        # the `*`/splat unpacks ("flattens") an iterable when building a list/tuple/…
        # for example, `[*[1, 2], *('a', 'b')]` creates `[1, 2, 'a', 'b']`
        *enumerate("ABC", start=1), *enumerate("XYZ", start=1)
    )
}
# ### Case 1 Score
# dicts allow for complex keys, they just may not be modifyable.
# We can use a tuple of the enemy and our move, as in (1, 1), (1, 2), …,
# to directly lookup move combinations and their score.
MOVE_SCORE = {
    (enemy_move, my_move): my_move + (
        (my_move - enemy_move + 1) % 3 * 3
    )
    for enemy_move in range(1, 4)
    for my_move in range(1, 4)
}


def sum_direct(moves: Iterator[tuple[int, int]]) -> int:
    return sum(MOVE_SCORE[move] for move in moves)


REACT_SCORE = {
    (enemy_move, my_move): my_move * 3 - 3 + (
        (my_move + enemy_move) % 3 + 1
    )
    for enemy_move in range(1, 4)
    for my_move in range(1, 4)
}


def sum_react(moves: Iterator[tuple[int, int]]) -> int:
    return sum(REACT_SCORE[move] for move in moves)


def solve(data: io.StringIO) -> tuple[Any, Any]:
    move_data = [
        (MOVE[enemy], MOVE[mine]) for enemy, _, mine in map(str.strip, data)
    ]
    return sum_direct(move_data), sum_react(move_data)
