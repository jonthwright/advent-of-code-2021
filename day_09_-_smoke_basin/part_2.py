#!/usr/bin/env python3

from typing import Tuple, Set
from collections import deque
import functools

def low_basin_points(basins: list[list[int]]) -> Set[Tuple[int, int]]:
	low_points = set()

	for i, row in enumerate(basins):
		for j, point in enumerate(row):
			min_adjacent = float('inf')

			for delta in range(-1, 2, 2):
				row_delta = i + delta
				if 0 <= row_delta < len(basins):
					min_adjacent = min(min_adjacent, basins[row_delta][j])

			for delta in range(-1, 2, 2):
				col_delta = j + delta
				if 0 <= col_delta < len(basins[i]):
					min_adjacent = min(min_adjacent, basins[i][col_delta])

			if point < min_adjacent:
				low_points.add((i, j))			
   
	return low_points

def solution(elements: list[list[int]]) -> int:
	low_points = low_basin_points(elements)
	basin_sizes = [0] * 3

	for x, y in low_points:
		basin_neighbours = deque([(x, y)])
		basin_points = set()

		while basin_neighbours:
			current_point = current_x, current_y = basin_neighbours.pop()
			if elements[current_x][current_y] == 9:
				continue

			basin_points.add(current_point)

			for delta in range(-1, 2, 2):
				adjacent_x = current_x + delta
				if 0 <= adjacent_x < len(elements) and (adjacent_x, current_y) not in basin_points:
					basin_neighbours.append((adjacent_x, current_y))

			for delta in range(-1, 2, 2):
				adjacent_y = current_y + delta
				if 0 <= adjacent_y < len(elements[current_x])  and (current_x, adjacent_y) not in basin_points:
					basin_neighbours.append((current_x, adjacent_y))
		
		basin_size = len(basin_points)
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
 