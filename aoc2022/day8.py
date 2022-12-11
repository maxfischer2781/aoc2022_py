from typing import Any, Iterator
import io


Map = tuple[tuple[int]]


def find_height_edges(forest: Iterator[Iterator[int]]):
    for line in forest:
        seen: list[int | None] = [None for _ in range(10)]
        for index, height in enumerate(line):
            if seen[height] is None:
                seen[height] = index
                for smaller in range(height):
                    if seen[smaller] is None:
                        seen[smaller] = -1
        yield [index if index != -1 else None for index in seen]


def find_visible(edge_left, edge_right, edge_top, edge_bottom, size: int):
    visible = set()
    for line_idx, row_indices in enumerate(edge_left):
        visible.update(
            (line_idx, row_idx) for row_idx in row_indices if row_idx is not None
        )
    for line_idx, row_indices in enumerate(edge_right):
        visible.update(
            (line_idx, size - row_idx - 1) for row_idx in row_indices if row_idx is not None
        )
    for row_idx, line_indices in enumerate(edge_top):
        visible.update(
            (line_idx, row_idx) for line_idx in line_indices if line_idx is not None
        )
    for row_idx, line_indices in enumerate(edge_bottom):
        visible.update(
            (size - line_idx - 1, row_idx) for line_idx in line_indices if line_idx is not None
        )
    return len(visible)


def scenic_score(down: int, right: int, forest: Map) -> int:
    own_height = forest[down][right]
    score = 1
    for line in (
        (row[right] for row in forest[:down][::-1]),  # up
        forest[down][:right][::-1],  # left
        forest[down][right+1:],  # right
        (row[right] for row in forest[down+1:]),  # down
    ):
        distance = 0
        for distance, height in enumerate(line, start=1):
            if height >= own_height:
                break
        score *= distance
    return score


def solve(data: io.StringIO) -> tuple[Any, Any]:
    board = tuple(tuple(int(tree) for tree in line.strip()) for line in data)
    edge_left = tuple(find_height_edges(board))
    edge_right = tuple(find_height_edges(reversed(line) for line in board))
    edge_top = tuple(find_height_edges(zip(*board)))
    edge_bottom = tuple(find_height_edges(reversed(line) for line in zip(*board)))
    size = len(board)
    max_score = max(
        scenic_score(down, right, board)
        for down in range(1, size)
        for right in range(1, size)
    )
    return find_visible(edge_left, edge_right, edge_top, edge_bottom, size), max_score
