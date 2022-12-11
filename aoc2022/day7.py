from typing import Any, Iterator
from collections import defaultdict
import io

Directory = "dict[str, int | Directory]"
ROOT = "/"


def nested_default_dict():
    return defaultdict(nested_default_dict)


def undefault(d: Directory) -> Directory:
    return {
        key: value if not isinstance(value, dict) else undefault(value)
        for key, value in d.items()
    }


def read_tree(data: io.StringIO) -> Directory:
    tree = nested_default_dict()
    location = [ROOT]
    for line in data:
        if line.startswith("$ cd"):
            target = line.split()[-1].strip()
            if target == ROOT:
                location = [ROOT]
            elif target == "..":
                location.pop()
            else:
                location.append(target)
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            pass
        else:
            size, name = line.split()
            cwd = tree
            for directory in location:
                cwd = cwd[directory]
            cwd[name] = int(size)
    return undefault(tree)


# TODO: write as generator using `yield from`
def directory_size(tree: Directory, location: str, seen: dict) -> int:
    total = 0
    for child, content in tree.items():
        if not isinstance(content, dict):
            total += content
        else:
            total += directory_size(content, location + "/" + child, seen=seen)
    seen[location if location else "/"] = total
    return total


def solve(data: io.StringIO) -> tuple[Any, Any]:
    tree = read_tree(data)
    directory_sizes = {}
    directory_size(tree[ROOT], '', directory_sizes)
    required = 30000000 - (70000000 - directory_sizes[ROOT])
    return sum(size for size in directory_sizes.values() if size <= 100000), min(
        size for size in directory_sizes.values() if size >= required
    )
