#!/usr/bin/env python3

import os


def movement(seafloor, sea_cucumber_direction, movement_func):
	sea_cucumbers_moved = False
	new_seafloor = {}

	for position in seafloor:
		if sea_cucumber_direction == seafloor[position]:
			new_position = movement_func(*position)
			if new_position not in seafloor:
				sea_cucumbers_moved = True
				new_seafloor[new_position] = sea_cucumber_direction
			else:
				new_seafloor[position] = sea_cucumber_direction
		else:
			new_seafloor[position] = seafloor[position]

	return sea_cucumbers_moved, new_seafloor

def solution(elements: list[list[str]]) -> int:
	rows, columns = len(elements), len(elements[0])
	seafloor = {(x, y) : elements[y][x] for y in range(rows) for x in range(columns) if elements[y][x] != '.'}
	eastwards = lambda x, y: ((x + 1) % columns, y)
	southwards = lambda x, y: (x, (y + 1) % rows)
	blocked = False
	sea_cucumbers_movements = 0

	while not blocked:
		sea_cucumbers_movements += 1
		moved_east, seafloor = movement(seafloor, '>', eastwards)
		moved_south, seafloor = movement(seafloor, 'v', southwards)
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
