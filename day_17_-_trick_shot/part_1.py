#!/usr/bin/env python3

import os
import re


def solution(elements: tuple[int, int, int, int]) -> int:
	_, _, min_y, _ = elements
	max_height = (min_y * (min_y + 1)) // 2

	return max_height


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = (int(values) for values in re.findall(r'(-?\d+)', f.readline().strip()))

	print('Day 17 : Trick Shot - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
