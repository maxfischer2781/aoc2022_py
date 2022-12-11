"""
Day 6 - Tuning Trouble

Another simple task if you know how to implement the key component: sliding windows.
This is a good use for Python's *generators*, since we can build a helper just for
iterating over the items seen by the sliding window. From there on it is enough to
solve the task ("are all items unique?") for one window and combine the two.

Note that while the sliding window helper is convenient, it is overkill for this.
Since we only ever look at a window of about a dozen items, creating and discarding
a string slice for each window would be more efficient. A sliding window generator
is useful especially when the input is streamed, e.g. it is too large for memory.
"""
from typing import Any, TypeVar, Iterable, Iterator
import io
from collections import deque


T = TypeVar("T")


def window(items: Iterable[T], n: int) -> Iterator[tuple[T, ...]]:
    """Create a sliding window of size n over some items"""
    # We need to keep state over two iterations, so we definitely need an iterator.
    iterator = iter(items)
    # We use a deque – a *d*ouble *e*nded *que*ue – which allows to efficiently
    # pop/append on both sides; this matches that each new window is created by
    # appending a new and pop'ing an old item.
    # The `maxlen` makes the deque pop the oldest item when we add a new one.
    buffer = deque([next(iterator) for _ in range(n-1)], maxlen=n)
    for item in iterator:
        buffer.append(item)
        yield buffer


def seek_marker(message: str, n: int) -> int:
    for idx, items in enumerate(window(message, n), start=n):
        # Since `set` only stores each item once, a `set` of a sequence containing
        # duplicate items is shorter than the sequence. In turn, if they have the
        # same size it means all items are unique.
        if len(set(items)) == n:
            return idx


def solve(data: io.StringIO) -> tuple[Any, Any]:
    message = next(data)
    return seek_marker(message, 4), seek_marker(message, 14)
