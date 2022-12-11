from __future__ import annotations
from typing import Any, Callable
import io
from copy import deepcopy
from math import prod
from dataclasses import dataclass


@dataclass
class Monkey:
    index: int
    items: list[int]
    operation: Callable[[int], int]
    test: int
    targets: tuple[int, int]

    # Monkey 0:
    #   Starting items: 79, 98
    #   Operation: new = old * 19
    #   Test: divisible by 23
    #     If true: throw to monkey 2
    #     If false: throw to monkey 3
    @classmethod
    def parse(cls, notes: io.StringIO) -> Monkey:
        index = int(next(notes).split()[-1][:-1])
        items = [int(item) for item in next(notes).split(':')[-1].split(',')]
        raw_operation = next(notes).split("=")[-1]
        operation = eval(f"lambda old: {raw_operation}")
        test, *targets = [int(next(notes).split()[-1]) for _ in range(3)]
        return cls(index, items, operation, test, tuple(targets))

    def take_turn(self, others: list[Monkey], bias: int):
        count = len(self.items)
        for item in self.items:
            score = self.operation(item) // bias
            target = self.targets[bool(score % self.test)]
            others[target].items.append(score)
        self.items.clear()
        return count


def parse(data: io.StringIO) -> list[Monkey]:
    monkeys = []
    while True:
        monkeys.append(Monkey.parse(data))
        if next(data, None) is None:
            break
    return monkeys


def simulate_turns(monkeys: list[Monkey], n: int, bias: int):
    assert all(monkey.index not in monkey.targets for monkey in monkeys)
    lcd = prod(monkey.test for monkey in monkeys)
    scores = [0 for _ in range(len(monkeys))]
    for _ in range(n):
        if _ % 100 == 0:
            print(_)
            print(monkeys)
        for index, monkey in enumerate(monkeys):
            scores[index] += monkey.take_turn(monkeys, bias)
        for monkey in monkeys:
            monkey.items = [item % lcd for item in monkey.items]
    return sorted(scores)[-2:]


def solve(data: io.StringIO) -> tuple[Any, Any]:
    monkeys = parse(data)
    most_busy = simulate_turns(deepcopy(monkeys), 20, 3)
    most_busy_10k = simulate_turns(monkeys, 10000, 1)
    return prod(most_busy), prod(most_busy_10k)
