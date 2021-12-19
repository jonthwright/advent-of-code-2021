#!/usr/bin/env python3

import os


def solution(elements: list[int]) -> int:
	cur_lanternfish_school = [0] * 9

	for lantern_timer in elements:
		cur_lanternfish_school[lantern_timer] += 1

	for _ in range(80):
		next_lanternfish_school = [0] * 9
		for lantern_timer in range(1, 9):
			next_lanternfish_school[lantern_timer - 1] = cur_lanternfish_school[lantern_timer]
		next_lanternfish_school[6] += cur_lanternfish_school[0]
		next_lanternfish_school[8] += cur_lanternfish_school[0]
		cur_lanternfish_school = [fish for fish in next_lanternfish_school]
  
	return sum(cur_lanternfish_school)


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [int(line) for line in f.readline().strip().split(',')]

	print('Day 06 : Lanternfish - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
