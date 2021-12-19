#!/usr/bin/env python3

import os
from collections import defaultdict

 
def solution(main_inputs: str, elements: list[str]) -> int:
	polymer_template = {polymer_pair : polymer_result for polymer_pair, polymer_result in elements}

	poly_pair = defaultdict(int)
	for i in range(len(main_inputs) - 1):
		poly_pair[main_inputs[i: i + 2]] +=  1

	for _ in range(40):
		new_poly_pair = defaultdict(int)
	
		for pair, poly_count in poly_pair.items():
			new_poly_with_left = pair[0] + polymer_template[pair]
			new_poly_with_right = polymer_template[pair] + pair[1]

			new_poly_pair[new_poly_with_left] += poly_count
			new_poly_pair[new_poly_with_right] += poly_count

		poly_pair = new_poly_pair

	gen_polymer = ''.join(set(poly_pair.keys()))
	polymer_quantity = {polymer : max(sum(count for (left, _), count in poly_pair.items() if polymer == left), 
                    	     			sum(count for (_, right), count in poly_pair.items() if polymer == right))
											for polymer in gen_polymer}

	max_polymer = max(polymer_quantity, key=polymer_quantity.get)
	min_polymer = min(polymer_quantity, key=polymer_quantity.get)


	return polymer_quantity[max_polymer] - polymer_quantity[min_polymer]


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		main_input, _, *inputs = [line.strip() for line in f.readlines()]
		inputs = [line.split(' -> ') for line in inputs]

	print('Day 14 : Extended Polymerisation - part 2')
	print(f'>>> Answer : {solution(main_input, inputs)}')

if __name__ == '__main__':
	main()
