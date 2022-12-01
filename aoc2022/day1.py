"""
Day 1 - Calorie Counting

This is a pretty simple input reading exercise. We get a lot of work for free
thanks to Python's builtin helper functions. The main challenge is parsing the
input: we must split it into blocks and calculate the totals per block.
```
1000  # 1000
2000  # 1000 + 2000
3000  # 1000 + 2000 + 3000
      # total: 6000
4000  # 4000
      # total: 4000
5000  # 5000
6000  # 5000 + 6000
      # total: 11000
```
This task can be done easily using a *generator function* – see `sum_calories`.
"""
from typing import Any, Iterator
import io


# Helper generator function to parse the data
def sum_calories(data: io.StringIO) -> Iterator[int]:
    """Sum up the calories per block/elf"""
    current = 0
    for line in data:
        if line == "\n" and current:
            yield current
            current = 0
        else:
            current += int(line)
    if current:
        yield current


def solve(data: io.StringIO) -> tuple[Any, Any]:
    # > we need the highest and three-highest calories
    # `sorted` provides us with a list of calories from lowest to highest.
    # We use subscription with a slice `[-3:]` to select only the three
    # final/highest entries of that list.
    top_calories = sorted(sum_calories(data))[-3:]
    return top_calories[-1], sum(top_calories)
