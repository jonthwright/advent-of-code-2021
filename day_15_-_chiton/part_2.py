#!/usr/bin/env python3

import os
import heapq as hq
from typing import Iterator


def generate_neighbours(x: int, y: int, width, height) -> Iterator[tuple[int, int]]:
	for dx in range(-1, 2):
		if 0 <= (new_x := x + dx) < width:
			for dy in range(-1, 2):
				if abs(dx) != abs(dy) and 0 <= (new_y := y + dy) < height: 
					yield new_x, new_y

def lowest_risk_path(chiton_risk_map: list[list[int]]) -> int | float:
	width, height = len(chiton_risk_map[-1]), len(chiton_risk_map)
	risk_path_heap = [(0, 0, 0)]

	while risk_path_heap:
		risk_score, x, y = hq.heappop(risk_path_heap)

		if (x, y) == (width - 1, height - 1):
			return risk_score

		for dx, dy in generate_neighbours(x, y, width, height):
			if chiton_risk_map[dy][dx] >= 0:
				new_risk_score = risk_score + chiton_risk_map[dy][dx]
				hq.heappush(risk_path_heap, (new_risk_score, dx, dy))
				chiton_risk_map[dy][dx] = -1

	return float('inf')

def expand_chiton_risk_map(chiton_risk_map: list[list[int]], scale_factor: int = 5) -> None:
	og_width, og_height = len(chiton_risk_map[0]), len(chiton_risk_map)

	for sf in range(scale_factor - 1):
		for y in range(og_height):
			chiton_risk_map.append([(risk % 9) + 1 for risk in chiton_risk_map[y + sf * og_height]])

	for sf in range(scale_factor - 1):
		for y in range(len(chiton_risk_map)):
			for x in range(og_width):
				chiton_risk_map[y].append((chiton_risk_map[y][x + sf * og_width] % 9) + 1)

def solution(elements: list[list[int]]) -> int | float:
	expand_chiton_risk_map(elements)
	return lowest_risk_path(elements)


def main():
	aoc_day_loc = os.path.dirname(__file__).replace('\\', '/')
	with open(f'{aoc_day_loc}/input_file.txt', 'r') as f:
		inputs = [[int(col) for col in row.strip()] for row in f.readlines()]
	print('Day 15 : Chiton - part 2')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()	
