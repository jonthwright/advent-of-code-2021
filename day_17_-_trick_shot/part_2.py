#!/usr/bin/env python3

import os
import re


def hit_target(velocity_x: int, velocity_y: int, min_x: int, max_x: int, min_y: int, max_y: int) -> bool:
	displacement_x = displacement_y = 0

	while abs(displacement_x) <= max(abs(min_x), abs(max_x)) and displacement_y >= min_y:
		if min_x <= displacement_x <= max_x and min_y <= displacement_y <= max_y:
			return True

		displacement_x += velocity_x
		displacement_y += velocity_y
		velocity_x += 1 * (velocity_x < 0) + -1 * (velocity_x > 0)
		velocity_y -= 1

	return False

def solution(elements: tuple[int, int, int, int]) -> int:
	min_x, max_x, min_y, max_y = elements
	hit_counter = 0

	for velocity_x in range(max(max_x, 0) + 1):
		for velocity_y in range(min_y, abs(max_y) * 2 + 1):
			hit_counter += hit_target(velocity_x, velocity_y, min_x, max_x, min_y, max_y)
	
	return hit_counter


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = (int(values) for values in re.findall(r'(-?\d+)', f.readline().strip()))

	print('Day 17 : Trick Shot - part 2')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
