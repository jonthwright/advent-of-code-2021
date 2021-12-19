#!/usr/bin/env python3

import os
from collections import deque
from typing import Iterator


def generate_neighbours(x: int, y: int, width, height) -> Iterator[tuple[int, int]]:
	for dx in range(-1, 2):
		if 0 <= (new_x := x + dx) < width:
			for dy in range(-1, 2):
				if abs(dx) != abs(dy) and 0 <= (new_y := y + dy) < height: 
					yield new_x, new_y


def solution(elements: list[list[int]]) -> int:
	end_point = (len(elements[-1]) - 1, len(elements) - 1)

	risk_path_queue = deque([end_point])
	chiton_risk_dict = {end_point : 0}

	while risk_path_queue:
		x, y = risk_path_queue.popleft()
		current_risk_score = chiton_risk_dict[(x, y)] + elements[y][x]

		for dx, dy in generate_neighbours(x, y, len(elements[y]), len(elements)):	
			if (dx, dy) not in chiton_risk_dict or chiton_risk_dict[(dx, dy)] > current_risk_score:
				risk_path_queue.append((dx, dy))
				chiton_risk_dict[(dx, dy)] = current_risk_score

	return chiton_risk_dict[(0, 0)]


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [[int(col) for col in row.strip()] for row in f.readlines()]

	print('Day 15 : Chiton - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()	
