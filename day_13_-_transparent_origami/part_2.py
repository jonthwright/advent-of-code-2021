#!/usr/bin/env python3

import os


def origami_points_stringified(origami: set[tuple[int, int]]) -> str:
	xs = {x for x, _ in origami}
	ys = {y for _, y in origami}

	origami_string = ''

	for y in range(min(ys), max(ys) + 1):
		origami_string += ''.join('#' if (x, y) in origami else ' ' for x in range(min(xs), max(xs) + 1))
		origami_string += '\n'

	return origami_string[:len(origami_string) - 1]

def solution(elements: list[tuple[int, int]], instructions: list[str]) -> str:
	origami = set(elements)

	for flip_direction, fold_target in instructions:
		for x, y in origami.copy():
			if flip_direction == 'x' and x >= fold_target:
				origami.remove((x, y))
				origami.add((fold_target * 2 - x, y))
			if flip_direction == 'y' and y >= fold_target:
				origami.remove((x, y))
				origami.add((x, fold_target * 2 - y))

	return origami_points_stringified(origami)


def main():
	aoc_day_loc = os.path.dirname(__file__).replace('\\', '/')

	main_inputs, additional_inputs = [], []
	main_input = True

	with open(f'{aoc_day_loc}/input_file.txt', 'r') as f:
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
