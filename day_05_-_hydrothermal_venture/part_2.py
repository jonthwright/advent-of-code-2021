# #!/usr/bin/env python3
		
from collections import defaultdict

def solution(elements: list[list[int]]) -> int:
	lines = defaultdict(lambda: 0)

	for x0, y0, x1, y1 in elements:
		if x0 == x1:
			for y_ in range(min(y0, y1), max(y0, y1) + 1):
				lines[(x0, y_)] += 1
		elif y0 == y1:
			for x_ in range(min(x0, x1), max(x0, x1) + 1):
				lines[(x_, y0)] += 1
		else:
			dx = (x1 - x0) // abs(x1 - x0)			
			dy = (y1 - y0) // abs(y1 - y0)

			lines[(x0, y0)] += 1
			while x0 != x1 and y0 != y1:
				x0 += dx
				y0 += dy
				lines[(x0, y0)] += 1

	return len([l for l in lines.values() if l > 1])


def main():
	with open('input_file.txt', 'r') as f:
		inputs = [line.strip('\n').split(' -> ') for line in f.readlines()]
		inputs = [tuple(int(point) for points in line for point in points.split(',')) for line in inputs]
	print('Day 05 : Hydrothermal Venture - part 2')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
