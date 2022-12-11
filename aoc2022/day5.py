"""
Day 5 - Supply Stacks

This task is not that complicated, but it is the first time we deal with different
inputs and parse a "human readable" format. Solving the actual task boils down to
treating lists as a *stack* (via append/pop) or a sequence (via slicing/extend).
"""
from typing import Any
from itertools import zip_longest
from copy import deepcopy
import io


Stacks = list[list[str]]
Instruction = tuple[int, int, int]


def parse(data: io.StringIO) -> tuple[Stacks, list[Instruction]]:
    """Parse the input to separate starting stacks and a sequence of instructions"""
    stacks = []
    for line in data:
        # The stacks and instructions are separated by a newline. Since `data` is an
        # iterator, it keeps its state when we break out of the loop. The next loop
        # will proceed where this one ended.
        if line == "\n":
            break
        # The input looks visually nice but is actually well formalised. If we look at
        # one line, we see a regular format
        # input: [F] [M] [H] [C] [S] [T] [N] [N] [N]
        # index:  1   5   9
        # We can get all of these as a slice line[1::4] to get the crate at position 1,
        # then each further crate 4 positions later.
        for crate, stack in zip_longest(line[1::4], stacks):
            if stack is None:
                stacks.append(stack := [])
            if crate != ' ':
                stack.append(crate)
    # We need to post-process the parsed stack to invert them.
    # Alternatively, we could invert some of the logic later on.
    for stack in stacks:
        stack[:] = stack[:-1][::-1]
    instructions = []
    for line in data:
        # move 1 from 5 to 2
        instructions.append(tuple(int(field) for field in line.split()[1::2]))
    return stacks, instructions


def simulate_single(stacks: Stacks, instructions: list[Instruction]):
    for count, source, target in instructions:
        for _ in range(count):
            stacks[target - 1].append(stacks[source-1].pop())
    return ''.join(stack[-1] for stack in stacks)


def simulate_group(stacks: Stacks, instructions: list[Instruction]):
    for count, source, target in instructions:
        stacks[target - 1].extend(stacks[source-1][-count:])
        stacks[source - 1][-count:] = []
    return ''.join(stack[-1] if stack else ' ' for stack in stacks)


def solve(data: io.StringIO) -> tuple[Any, Any]:
    stacks, instructions = parse(data)
    return (
        simulate_single(deepcopy(stacks), instructions),
        simulate_group(deepcopy(stacks), instructions),
    )
