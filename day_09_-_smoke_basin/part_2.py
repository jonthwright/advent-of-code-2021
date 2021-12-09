#!/usr/bin/env python3

from typing import Tuple, Set
from collections import deque

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
	largest, second_largest, third_largest = 0, sum(sum(elem) for elem in elements), 1

	for x, y in low_points:
		basin_stack = deque([(x, y)])
		basin_points = set()

		while basin_stack:
			current_point = current_x, current_y = basin_stack.pop()
			if elements[current_x][current_y] == 9:
				continue

			basin_points.add(current_point)

			for delta in range(-1, 2, 2):
				adjacent_x = current_x + delta
				if 0 <= adjacent_x < len(elements) and (adjacent_x, current_y) not in basin_points:
					basin_stack.append((adjacent_x, current_y))

			for delta in range(-1, 2, 2):
				adjacent_y = current_y + delta
				if 0 <= adjacent_y < len(elements[current_x])  and (current_x, adjacent_y) not in basin_points:
					basin_stack.append((current_x, adjacent_y))

		if largest < (basin_size := len(basin_points)):
			largest, second_largest, third_largest = basin_size, largest, second_largest
		elif second_largest < basin_size:
			second_largest, third_largest = basin_size, second_largest
		elif third_largest < basin_size:
			third_largest = basin_size
			
	return largest * second_largest * third_largest


def main():
	with open('input_file.txt', 'r') as f:
		inputs = [[int(col) for col in row.strip()] for row in f.readlines()]
	print('Day 09 : Smoke Basin - part 2')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
 