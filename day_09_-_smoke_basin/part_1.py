#!/usr/bin/env python3

def solution(elements: list[list[int]]) -> int:
	risk_level = 0

	for x in range(len(elements)):
		for y, low_point in enumerate(elements[x]):
			min_adjacent = float('inf')

			for delta in range(-1, 2, 2):
				x_delta = x + delta
				if 0 <= x_delta < len(elements):
					min_adjacent = min(min_adjacent, elements[x_delta][y])

			for delta in range(-1, 2, 2):
				y_delta = y + delta
				if 0 <= y_delta < len(elements[x]):
					min_adjacent = min(min_adjacent, elements[x][y_delta])

			is_low_point = low_point < min_adjacent
			risk_level += (low_point * is_low_point) + is_low_point
   
	return risk_level


def main():
	with open('input_file.txt', 'r') as f:
		inputs = [[int(col) for col in row.strip()] for row in f.readlines()]
	print('Day 09 : Smoke Basin - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
 