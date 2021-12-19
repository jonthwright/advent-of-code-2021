#!/usr/bin/env python3

import os


def solution(elements: list[int]) -> int:
	return sum(sum(elements[i: i + 3]) < sum(elements[i + 1: i + 4]) for i in range(len(elements)))


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [int(line.strip()) for line in f.readlines()]

	print('Day 01 : Sonar Sweep - part 2')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()