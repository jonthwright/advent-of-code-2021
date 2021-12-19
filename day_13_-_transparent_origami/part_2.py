#!/usr/bin/env python3

import os
import operator


def origami_code_word(origami: set[tuple[int, int]]) -> str:
	min_x = min_y = float('inf')
	max_x = max_y = 0

	for points in origami:
		min_x = min(points[0], min_x)
		min_y = min(points[1], min_y)
		max_x = max(points[0], max_x)
		max_y = max(points[1], max_y)

	origami_string = ''

	for y in range(min_y, max_y + 1):
		origami_string += ''.join('█' if (x, y) in origami else ' ' for x in range(min_x, max_x + 1))
		origami_string += '\n' if y < max_y else ''

	return origami_string

def solution(elements: list[tuple[int, int]], instructions: list[str]) -> str:
	origami = set(elements)

	for flip_direction, fold_target in instructions:
		for x, y in origami.copy():
			if flip_direction == 'x' and x > fold_target:
				origami.remove((x, y))
				origami.add((fold_target * 2 - x, y))
			if flip_direction == 'y' and y > fold_target:
				origami.remove((x, y))
				origami.add((x, fold_target * 2 - y))

	return origami_code_word(origami)


def main():
	aoc_day_loc = os.path.dirname(__file__)

	main_inputs, additional_inputs = [], []
	main_input = True

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		for line in f.readlines():
			if line == '\n':
				main_input = False
				continue

			if main_input:
				main_inputs.append(tuple(int(value) for value in line.strip().split(',')))
			else:
				_, _, instruction = line.strip().split()
				cmd, value = instruction.split('=')
				additional_inputs.append((cmd, int(value)))
				
	print('Day 13 : Transparent Origami - part 2')
	print(f'>>> Answer :')
	print(solution(main_inputs, additional_inputs))

if __name__ == '__main__':
	main()
