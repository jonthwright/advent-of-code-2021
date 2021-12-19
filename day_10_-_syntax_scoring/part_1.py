#!/usr/bin/env python3

import os


def solution(elements: list[str]) -> int:
	bracket_dict = {
		'(' : ')',
		'[' : ']',
		'{': '}',
		'<': '>'
	}

	bracket_error_points = {
		')' : 3,
		']' : 57,
		'}' : 1197,
		'>' : 25137
	}

	syntax_error_score = 0

	for bracket_line in elements:
		bracket_stack = []

		for bracket in bracket_line:
			if bracket in bracket_dict:
				bracket_stack.append(bracket)
			else:
				pop_bracket_stack = bracket_stack.pop()
				syntax_error_score += bracket_error_points[bracket] * (bracket_dict[pop_bracket_stack] != bracket)
	
	return syntax_error_score


def main():
	aoc_day_loc = os.path.dirname(__file__).replace('\\', '/')

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [row.strip() for row in f.readlines()]

	print('Day 10 : Syntax Scoring - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
 