from typing import Any, TypeVar, Iterable, Iterator
import io


T = TypeVar("T")


def window(items: Iterable[T], n: int) -> Iterator[tuple[T, ...]]:
    iterator = iter(items)
    buffer = [next(iterator) for _ in range(n-1)]
    for item in iterator:
        buffer.append(item)
        yield buffer
        buffer.pop(0)


def seek_marker(message: str, n: int) -> int:
    for idx, items in enumerate(window(message, n), start=n):
        if len(set(items)) == n:
            return idx
    raise ValueError


def solve(data: io.StringIO) -> tuple[Any, Any]:
    message = next(data)
    return seek_marker(message, 4), seek_marker(message, 14)
