#!/usr/bin/env python3

import os


def solution(elements: list[str]) -> str:
	pairs = [(int(elements[18 * i + 5].split()[2]), int(elements[18 * i + 15].split()[2])) for i in range(14)]
	stack = []
	links = {}

	for i, (a, b) in enumerate(pairs):
		if a > 0:
			stack.append((i, b))
		else:
			j, bj = stack.pop()
			links[i] = (j, bj + a)

	assignments = [0] * (max(links) + 1)

	for i, (j, delta) in links.items():
		assignments[i] = min(9, 9 + delta)
		assignments[j] = min(9, 9 - delta)

	return "".join(str(assignments[x]) for x in range(14))


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [row.strip() for row in f.readlines()]

	print('Day 24 : Arithmetic Logic Unit - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
