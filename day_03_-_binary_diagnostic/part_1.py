#!/usr/bin/env python3

import os
import functools


def solution(elements: list[int]) -> int:
	half_elem_num = len(elements) // 2
	max_bit_length = max(elements).bit_length()
	gamma_rate = 0

	for offset in range(max_bit_length, -1, -1):
		ones_counter = functools.reduce(lambda x, y: x + ((y >> offset) & 1), elements, 0)
		gamma_rate |= (ones_counter > half_elem_num) << offset
	
	epsilon_rate = gamma_rate ^ (2 ** max_bit_length - 1)
 
	return gamma_rate * epsilon_rate


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [int(line.strip(), 2) for line in f.readlines()]

	print('Day 03 : Binary Diagnostics - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()