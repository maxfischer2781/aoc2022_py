"""
Day 7

This is an exercise of working with tree data. Building on the simple *generator*
we used on Day 6 for handling *sequential* data, this is a nice excuse of using
a more complex generator to handle *nested* data. Specifically, we use a generator's
`return` and `yield from` statement.

More description to follow...
"""
from typing import Any, Generator
from collections import defaultdict
import io

Directory = "dict[str, int | Directory]"
ROOT = ""


def nested_default_dict():
    """An infinitely nested `defaultdict`"""
    return defaultdict(nested_default_dict)


def undefault(d: Directory) -> Directory:
    """Turn a nested defaultdict into a nested dict"""
    return {
        key: value if not isinstance(value, dict) else undefault(value)
        for key, value in d.items()
    }


def read_tree(data: io.StringIO) -> Directory:
    """Parse the tree input data format"""
    # This combines parsing the commands (cd, ls, ...)
    # with a minimal representation of ...
    # ... the location where we `cd`'d to last, and...
    location = [ROOT]
    # ... the file system tree we `ls`'d so far.
    tree = nested_default_dict()
    for line in data:
        # `cd` changes our current location in the file system.
        # This is effectively a stack, which we can either...
        if line.startswith("$ cd"):
            target = line.split()[-1].strip()
            # ... reset to the root location, ...
            if target == "/":
                location = [ROOT]
            # ... go up one level, or ...
            elif target == "..":
                location.pop()
            # ... descend to a specific child directory.
            else:
                location.append(target)
        # We can ignore all cases but `ls` output.
        elif not line.startswith("$") and not line.startswith("dir"):
            size, name = line.split()
            cwd = tree
            for directory in location:
                cwd = cwd[directory]
            cwd[name] = int(size)
    return undefault(tree)


def directory_size(
    tree: Directory, location: str
) -> Generator[tuple[str, int], None, int]:
    """Generator aggregating per-directory sizes"""
    # This generator uses a boring part of a `for` loop to keep a total,
    # combined with a complex part of nested generators' `return`+`yield from`.
    # The end result is that
    # a) the outermost consumer (think `for` loop) gets *all individual* results,
    #    even from nested generators, and
    # b) the inner consumers (instances of this generator) get *only the total* of
    #    nested results.
    total = 0
    for child, content in tree.items():
        if not isinstance(content, dict):
            total += content
        else:
            # The `yield from` does two things here:
            # - It passes on `yield` results from the nested `directory_size`.
            #   including all results passed on by it from deeply nested ones.
            # - It receives the `return` result from the nested `directory_size`.
            total += yield from directory_size(content, location + "/" + child)
    # `yield` the total for each location.
    # Since each nested `directory_size` gets invoked via `yield from`, these
    # pairs end up at the outermost consumer.
    yield location, total
    # `return` the total for this location and its children.
    # Since each nested `directory_size` gets invoked via `yield from`, this
    # ends up at the parent of the current location.
    # A generator-`return` value is ignored by a `for` loop, so the outermost consumer
    # does not have to care that we internally pass on this total.
    return total


def solve(data: io.StringIO) -> tuple[Any, Any]:
    tree = read_tree(data)
    directory_sizes = dict(directory_size(tree[ROOT], ''))
    required = 30000000 - (70000000 - directory_sizes[ROOT])
    return sum(size for size in directory_sizes.values() if size <= 100000), min(
        size for size in directory_sizes.values() if size >= required
    )
