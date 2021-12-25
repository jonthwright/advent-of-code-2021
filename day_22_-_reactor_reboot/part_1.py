#!/usr/bin/env python3

import os
import re


def solution(elements: list[tuple[str, int, int, int, int, int, int]]) -> int:
	on_cubes = {}

	for cube, x_min, x_max, y_min, y_max, z_min, z_max in elements:
		for x in range(max(x_min, -50), min(x_max, 50) + 1):
			for y in range(max(y_min, -50), min(y_max, 50) + 1):
				for z in range(max(z_min, -50), min(z_max, 50) + 1):
					on_cubes[(x, y, z)] = cube == 'on'

	return sum(on_cubes.values())


def parse_inputs(inputs: str) -> tuple[str, int, int, int, int, int, int]:
	str_input, int_inputs = inputs.split(' ')
	int_inputs = list(int(input_ints) for input_ints in re.findall(r'(-?\d+)', int_inputs))
	return str_input, *int_inputs

def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [parse_inputs(row.strip()) for row in f.readlines()]

	print('Day 22 : Reactor Reboot - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
