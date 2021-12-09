#!/usr/bin/env python3

from typing import Tuple, Set
import functools

def get_basin_size(basins: list[list[int]], x: int, y: int) -> None:
	if basins[x][y] == -1 or basins[x][y] == 9:
		return 0

	basin_neighbours = [(x, y)]
	basins[x][y] = -1
	basin_size = 0

	while basin_neighbours:
		x, y = basin_neighbours.pop()
		basin_size += 1

		for delta in range(-1, 2, 2):
			x_delta = x + delta
			if 0 <= x_delta < len(basins) and 0 <= basins[x_delta][y] < 9:
				basin_neighbours.append((x_delta, y))
				basins[x_delta][y] = -1

		for delta in range(-1, 2, 2):
			y_delta = y + delta
			if 0 <= y_delta < len(basins[x]) and 0 <= basins[x][y_delta] < 9:
				basin_neighbours.append((x, y_delta))
				basins[x][y_delta] = -1

	return basin_size


def solution(elements: list[list[int]]) -> int:
	basin_sizes = [0] * 3
	basin_size = 0

	for x in range(len(elements)):
		for y in range(len(elements[x])):
			if elements[x][y] != -1 or elements[x][y] != 9:
				basin_size = get_basin_size(elements, x, y)
			if basin_sizes[0] < basin_size:
				basin_sizes[0], basin_sizes[1:] = basin_size, basin_sizes[0:2]
			elif basin_sizes[1] < basin_size:
				basin_sizes[1], basin_sizes[2] = basin_size, basin_sizes[1]
			elif basin_sizes[2] < basin_size:
				basin_sizes[2] = basin_size

	return functools.reduce(lambda x, y: x * y, basin_sizes)


def main():
	with open('input_file.txt', 'r') as f:
		inputs = [[int(col) for col in row.strip()] for row in f.readlines()]
	print('Day 09 : Smoke Basin - part 2')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
 