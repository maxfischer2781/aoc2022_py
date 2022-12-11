from typing import Any, Iterator
import io

Instructions = list[int | None]


def parse(data: io.StringIO) -> Instructions:
    return [
        int(line.split()[-1]) if line.startswith("addx") else None
        for line in data
    ]


def simulate_register(instructions: Instructions, start: int = 1) -> Iterator[int]:
    register = start
    for instruction in instructions:
        if instruction is None:
            yield register
        else:
            yield register
            yield register
            register += instruction


def simulate_20(instructions: Instructions) -> int:
    accumulated = 0
    for cycle, register in enumerate(simulate_register(instructions, 1), start=1):
        if cycle % 40 == 20:
            accumulated += register * cycle
        if cycle > 220:
            break
    return accumulated


def simulate_crt(instructions: Instructions) -> list[int]:
    screen = []
    for cycle, register in enumerate(simulate_register(instructions, 0), start=0):
        screen.append(register <= cycle % 40 <= register + 2)
    return screen


def solve(data: io.StringIO) -> tuple[Any, Any]:
    instructions = parse(data)
    # TODO: Automate reading to string
    # ###..####.###...##....##.####.#....#..#.
    # #..#....#.#..#.#..#....#.#....#....#.#..
    # ###....#..#..#.#..#....#.###..#....##...
    # #..#..#...###..####....#.#....#....#.#..
    # #..#.#....#....#..#.#..#.#....#....#.#..
    # ###..####.#....#..#..##..####.####.#..#.
    screen = simulate_crt(instructions)
    for idx, lit in enumerate(screen):
        if idx % 40 == 0:
            print()
        print("#" if lit else ".", end="")
    return simulate_20(instructions), 0
