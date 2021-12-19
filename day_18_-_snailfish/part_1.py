#!/usr/bin/env python3

import os
import functools


Snailfishs = int | list | None

def explode(snailfish: Snailfishs, depth: int = 4) -> tuple[bool, Snailfishs, Snailfishs, Snailfishs]:
    if isinstance(snailfish, int):
        return False, None, snailfish, None

    a, b = snailfish
    if depth == 0:
        return True, snailfish[0], 0, snailfish[1]

    exploded, left, a, right = explode(a, depth - 1)
    if exploded:
        return True, left, [a, add_left(b, right)], None

    exploded, left, b, right = explode(b, depth - 1)
    if exploded:
        return True, None, [add_right(a, left), b], right

    return False, None, snailfish, None

def split(snailfish: Snailfishs) ->  tuple[bool, Snailfishs]:
	if isinstance(snailfish, int):
		if snailfish >= 10:
			return True, [snailfish // 2, (snailfish + 1) // 2]
		return False, snailfish

	left, right = snailfish

	changed, left = split(left)
	if changed:
		return True, [left, right]

	changed, right = split(right)

	return changed, [left, right]

def add_left(snailfish: Snailfishs, new: Snailfishs) -> Snailfishs:
	if new is None:
		return snailfish
	if isinstance(snailfish, int):
		return snailfish + new

	left, right = snailfish
	return [add_left(left, new), right]

def add_right(snailfish: Snailfishs, new: Snailfishs) -> Snailfishs:
	if new is None:
		return snailfish
	if isinstance(snailfish, int):
		return snailfish + new

	left, right = snailfish
	return [left, add_right(right, new)]

def add(left: Snailfishs, right: Snailfishs) -> Snailfishs:
	snailfish = [left, right]

	while True:
		changed, _, snailfish, _ = explode(snailfish)
		if changed:
			continue

		changed, snailfish = split(snailfish)
		if not changed:
			break

	return snailfish

def magnitude(snailfish: Snailfishs) -> int:
	if isinstance(snailfish, int):
		return snailfish

	left, right = snailfish
	return 3 * magnitude(left) + 2 * magnitude(right)

def solution(elements: list[str]) -> int:
	return magnitude(functools.reduce(add, [eval(e) for e in elements]))


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [line.strip() for line in f.readlines()]

	print('Day 18 : Snailfish - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
