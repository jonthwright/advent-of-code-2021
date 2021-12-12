#!/usr/bin/env python3

import os


def solution(elements: list[list[int]]) -> int:
	risk_level = 0

	for y in range(len(elements)):
		for x, low_point in enumerate(elements[y]):
			min_adjacent = float('inf')

			for delta in range(-1, 2, 2):
				dy = y + delta
				if 0 <= dy < len(elements):
					min_adjacent = min(min_adjacent, elements[dy][x])

			for delta in range(-1, 2, 2):
				dx = x + delta
				if 0 <= dx < len(elements[y]):
					min_adjacent = min(min_adjacent, elements[y][dx])

			is_low_point = low_point < min_adjacent
			risk_level += (low_point * is_low_point) + is_low_point
   
	return risk_level


def main():
	aoc_day_loc = os.path.dirname(__file__).replace('\\', '/')
	with open(f'{aoc_day_loc}/input_file.txt', 'r') as f:
		inputs = [[int(col) for col in row.strip()] for row in f.readlines()]
	print('Day 09 : Smoke Basin - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
 