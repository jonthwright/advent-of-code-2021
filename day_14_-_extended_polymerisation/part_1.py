#!/usr/bin/env python3

import os
from collections import defaultdict


def solution(main_inputs: str, elements: list[tuple[str, str]]) -> int:
	polymer_template = {polymer_pair : polymer_result for polymer_pair, polymer_result in elements}

	main_polymer_sequence, new_polymer_sequence = main_inputs, ''
	polymer_quantity = defaultdict(int)

	for _ in range(10):
		new_polymer_sequence = main_polymer_sequence[0]
		for i in range(len(main_polymer_sequence) - 1):
			left_polymer, right_polymer = main_polymer_sequence[i], main_polymer_sequence[i + 1]
			new_polymer_sequence += polymer_template[left_polymer + right_polymer] + right_polymer
		main_polymer_sequence = new_polymer_sequence

	for polymer in main_polymer_sequence:		
		polymer_quantity[polymer] += 1

	max_polymer = max(polymer_quantity, key=polymer_quantity.get)
	min_polymer = min(polymer_quantity, key=polymer_quantity.get)

	return polymer_quantity[max_polymer] - polymer_quantity[min_polymer]


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		main_input, _, *inputs = [line.strip() for line in f.readlines()]
		inputs = [line.split(' -> ') for line in inputs]

	print('Day 14 : Extended Polymerisation - part 1')
	print(f'>>> Answer : {solution(main_input, inputs)}')

if __name__ == '__main__':
	main()
