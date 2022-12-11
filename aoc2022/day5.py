from typing import Any
from itertools import zip_longest
from copy import deepcopy
import io


Stacks = list[list[str]]
Instruction = tuple[int, int, int]


def parse(data: io.StringIO) -> tuple[Stacks, list[Instruction]]:
    stacks = []
    for line in data:
        if line == "\n":  # stacks and instructions are separated by a newline
            break
        # first crate at position one, next is 4 further
        for crate, stack in zip_longest(line[1::4], stacks):
            if stack is None:
                stacks.append(stack := [])
            if crate != ' ':
                stack.append(crate)
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
