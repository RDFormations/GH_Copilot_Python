#!/usr/bin/env python3
"""
Standalone push_swap checker — single file, no dependency on student code.

Usage:
  python3 checker.py 3 1 2 < operations.txt
  python3 src/push_swap.py 3 1 2 | python3 checker.py 3 1 2

Prints OK or KO on stdout. Error on stderr + exit 1 for invalid input.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field

STACK_MAX = 50
VALID_OPS = frozenset(
    {"sa", "sb", "ss", "pa", "pb", "ra", "rb", "rr", "rra", "rrb", "rrr"}
)


class ParseError(Exception):
    pass


@dataclass
class Stack:
    values: list[int] = field(default_factory=list)


def stack_push(stack: Stack, value: int) -> None:
    if len(stack.values) >= STACK_MAX:
        raise RuntimeError("Stack overflow")
    stack.values.append(value)


def stack_pop(stack: Stack) -> int | None:
    return stack.values.pop() if stack.values else None


def stack_swap(stack: Stack) -> None:
    if len(stack.values) < 2:
        return
    stack.values[-1], stack.values[-2] = stack.values[-2], stack.values[-1]


def stack_rotate(stack: Stack) -> None:
    if len(stack.values) < 2:
        return
    top = stack.values.pop()
    stack.values.insert(0, top)


def stack_rev_rotate(stack: Stack) -> None:
    if len(stack.values) < 2:
        return
    bottom = stack.values.pop(0)
    stack.values.append(bottom)


def move_top(src: Stack, dst: Stack) -> None:
    value = stack_pop(src)
    if value is not None:
        stack_push(dst, value)


def is_sorted(stack: Stack) -> bool:
    for i in range(len(stack.values) - 1):
        if stack.values[i + 1] > stack.values[i]:
            return False
    return len(stack.values) > 0


def parse_args(argv: list[str]) -> list[int]:
    if not argv:
        return []

    values: list[int] = []
    for arg in argv:
        for token in arg.split():
            if not re.fullmatch(r"\+?\d+", token):
                raise ParseError("invalid integer")
            n = int(token)
            if n <= 0:
                raise ParseError("non-positive")
            if n in values:
                raise ParseError("duplicate")
            values.append(n)

    if len(values) < 2 or len(values) > STACK_MAX:
        raise ParseError("invalid count")

    return values


def stack_from_values(values: list[int]) -> Stack:
    stack = Stack(list(values))
    stack.values.reverse()
    return stack


def run_operation(name: str, a: Stack, b: Stack) -> None:
    match name:
        case "sa":
            stack_swap(a)
        case "sb":
            stack_swap(b)
        case "ss":
            stack_swap(a)
            stack_swap(b)
        case "pa":
            move_top(b, a)
        case "pb":
            move_top(a, b)
        case "ra":
            stack_rotate(a)
        case "rb":
            stack_rotate(b)
        case "rr":
            stack_rotate(a)
            stack_rotate(b)
        case "rra":
            stack_rev_rotate(a)
        case "rrb":
            stack_rev_rotate(b)
        case "rrr":
            stack_rev_rotate(a)
            stack_rev_rotate(b)


def read_instructions() -> list[str]:
    return [line.strip() for line in sys.stdin if line.strip()]


def main() -> None:
    args = sys.argv[1:]
    if not args:
        return

    try:
        values = parse_args(args)
    except ParseError:
        sys.stderr.write("Error\n")
        raise SystemExit(1) from None

    instructions = read_instructions()
    for op in instructions:
        if op not in VALID_OPS:
            sys.stderr.write("Error\n")
            raise SystemExit(1)

    a = stack_from_values(values)
    b = Stack()
    work_a = Stack(list(a.values))

    for op in instructions:
        run_operation(op, work_a, b)

    sys.stdout.write("OK\n" if is_sorted(work_a) and not b.values else "KO\n")


if __name__ == "__main__":
    main()
