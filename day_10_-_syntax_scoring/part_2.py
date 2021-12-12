#!/usr/bin/env python3

import os


def solution(elements: list[str]) -> int:
	bracket_dict = {
		'(' : ')',
		'[' : ']',
		'{': '}',
		'<': '>'
	}

	bracket_incomplete_points = {
		')' : 1,
		']' : 2,
		'}' : 3,
		'>' : 4
	}

	incomplete_bracket_scores = []

	for bracket_line in elements:
		bracket_stack = []
		corrupted = False

		for bracket in bracket_line:
			if bracket in bracket_dict:
				bracket_stack.append(bracket)
			else:
				pop_bracket_stack = bracket_stack.pop()
				if bracket_dict[pop_bracket_stack] != bracket:
					corrupted = True
					break

		if not corrupted:
			incomplete_score = 0
			for bracket in range(len(bracket_stack) - 1, -1, -1):
				incomplete_score *= 5
				incomplete_score += bracket_incomplete_points[bracket_dict[bracket_stack[bracket]]]
			incomplete_bracket_scores.append(incomplete_score)

	incomplete_bracket_scores.sort()
	middle_score_index = len(incomplete_bracket_scores) // 2

	return incomplete_bracket_scores[middle_score_index]


def main():
	aoc_day_loc = os.path.dirname(__file__).replace('\\', '/')
	with open(f'{aoc_day_loc}/input_file.txt', 'r') as f:
		inputs = [row.strip() for row in f.readlines()]
	print('Day 10 : Syntax Scoring - part 2')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
 