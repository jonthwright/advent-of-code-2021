#!/usr/bin/env python3

import os
import functools


def get_basin_size(basins: list[list[int]], x: int, y: int) -> None:
	if basins[y][x] == -1 or basins[y][x] == 9:
		return 0

	basin_neighbours = [(x, y)]
	basins[y][x] = -1
	basin_size = 0

	while basin_neighbours:
		x, y = basin_neighbours.pop()
		basin_size += 1

		for delta in range(-1, 2, 2):
			dx = x + delta
			if 0 <= dx < len(basins[y]) and 0 <= basins[y][dx] < 9:
				basin_neighbours.append((dx, y))
				basins[y][dx] = -1

		for delta in range(-1, 2, 2):
			dy = y + delta
			if 0 <= dy < len(basins) and 0 <= basins[dy][x] < 9:
				basin_neighbours.append((x, dy))
				basins[dy][x] = -1

	return basin_size


def solution(elements: list[list[int]]) -> int:
	basin_sizes = [0] * 3
	basin_size = 0

	for y in range(len(elements)):
		for x in range(len(elements[y])):
			if elements[y][x] != -1 or elements[y][x] != 9:
				basin_size = get_basin_size(elements, x, y)

			if basin_sizes[0] < basin_size:
				basin_sizes[0], basin_sizes[1:] = basin_size, basin_sizes[0:2]
			elif basin_sizes[1] < basin_size:
				basin_sizes[1], basin_sizes[2] = basin_size, basin_sizes[1]
			elif basin_sizes[2] < basin_size:
				basin_sizes[2] = basin_size

	return functools.reduce(lambda x, y: x * y, basin_sizes)


def main():
	aoc_day_loc = os.path.dirname(__file__).replace('\\', '/')

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [[int(col) for col in row.strip()] for row in f.readlines()]

	print('Day 09 : Smoke Basin - part 2')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
 