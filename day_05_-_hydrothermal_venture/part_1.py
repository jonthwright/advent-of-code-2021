# #!/usr/bin/env python3

import os		
from collections import defaultdict


def solution(elements: list[list[int]]) -> int:
	lines = defaultdict(int)

	for x0, y0, x1, y1 in elements:
		if x0 == x1:
			for dy in range(min(y0, y1), max(y0, y1) + 1):
				lines[(x0, dy)] += 1
		elif y0 == y1:
			for dx in range(min(x0, x1), max(x0, x1) + 1):
				lines[(dx, y0)] += 1
			
	return len([l for l in lines.values() if l > 1])


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [line.strip().split(' -> ') for line in f.readlines()]
		inputs = [tuple(int(point) for points in line for point in points.split(',')) for line in inputs]

	print('Day 05 : Hydrothermal Venture - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
