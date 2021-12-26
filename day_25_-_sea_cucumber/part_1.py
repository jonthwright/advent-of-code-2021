#!/usr/bin/env python3

import os
from typing import Callable


def sea_cucumber_movements(seafloor: dict[tuple[int, int], str], sea_cucumber_direction: str, movement_key: Callable[[int, int], int]) -> dict[tuple[int, int], str]:
	sea_cucumbers_moved = False
	new_seafloor = {}

	for sea_cucumber in seafloor:
		if sea_cucumber_direction == seafloor[sea_cucumber]:
			new_sea_cucumber = movement_key(*sea_cucumber)
			if new_sea_cucumber not in seafloor:
				sea_cucumbers_moved = True
				new_seafloor[new_sea_cucumber] = sea_cucumber_direction
			else:
				new_seafloor[sea_cucumber] = sea_cucumber_direction
		else:
			new_seafloor[sea_cucumber] = seafloor[sea_cucumber]

	return sea_cucumbers_moved, new_seafloor

def solution(elements: list[list[str]]) -> int:
	rows, columns = len(elements), len(elements[0])
	seafloor = {(x, y) : elements[y][x] for y in range(rows) for x in range(columns) if elements[y][x] != '.'}
	sea_cucumbers_movements = 0
	blocked = False

	while not blocked:
		sea_cucumbers_movements += 1

		moved_east, seafloor = sea_cucumber_movements(seafloor, '>', lambda x, y: ((x + 1) % columns, y))
		moved_south, seafloor = sea_cucumber_movements(seafloor, 'v', lambda x, y: (x, (y + 1) % rows))
		blocked = not moved_east and not moved_south
  
	return sea_cucumbers_movements
 

def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [row.strip() for row in f.readlines()]

	print('Day 25 : Sea Cucumber - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
