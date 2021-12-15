#!/usr/bin/env python3

import os


def solution(elements: list[list[int]]) -> int:
	end_point = (len(elements[-1]) - 1, len(elements) - 1)

	path_stack = [end_point]
	risk_map = {end_point : 0}

	while path_stack:
		x, y = path_stack.pop(0)
		current_risk_score = risk_map[(x, y)] + elements[y][x]

		for dy in range(-1, 2):
			for dx in range(-1, 2):
				if abs(dx) == abs(dy):
					continue

				dy += y
				dx += x	

				if not (0 <= dy < len(elements) and 0 <= dx < len(elements[y])):
					continue
	
				if (dx, dy) not in risk_map or risk_map[(dx, dy)] > current_risk_score:
					risk_map[(dx, dy)] = current_risk_score
					path_stack.append((dx, dy))

	return risk_map[(0, 0)]


def main():
	aoc_day_loc = os.path.dirname(__file__).replace('\\', '/')
	with open(f'{aoc_day_loc}/input_file.txt', 'r') as f:
		inputs = [[int(col) for col in row.strip()] for row in f.readlines()]
	print('Day 15 : Chiton - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()	
