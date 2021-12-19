#!/usr/bin/env python3

import os


def solution(elements: list[tuple[str, int]]) -> int:
	depth = horizontal = 0

	for op, unit in elements:
		match op:
			case 'down' : depth += unit
			case 'up' : depth -= unit
			case 'forward' : horizontal += unit
	return depth * horizontal

		
def main():
	aoc_day_loc = os.path.dirname(__file__).replace('\\', '/')

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [line.strip().split(' ') for line in f.readlines()]
		inputs = [(line[0], int(line[1])) for line in inputs]

	print('Day 02 : Dive! - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()