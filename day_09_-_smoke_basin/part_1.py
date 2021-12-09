#!/usr/bin/env python3

def solution(elements: list[list[int]]) -> int:
	risk_level = 0

	for i, row in enumerate(elements):
		for j, low_point in enumerate(row):
			min_adjacent = float('inf')

			for delta in range(-1, 2, 2):
				row_delta = i + delta
				if 0 <= row_delta < len(elements):
					min_adjacent = min(min_adjacent, elements[row_delta][j])

			for delta in range(-1, 2, 2):
				col_delta = j + delta
				if 0 <= col_delta < len(elements[i]):
					min_adjacent = min(min_adjacent, elements[i][col_delta])

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
 