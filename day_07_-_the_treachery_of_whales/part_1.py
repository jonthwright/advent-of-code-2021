#!/usr/bin/env python3

import os


def solution(elements: list[int]) -> int:
	best_fuel_cost = float('inf')

	for position in range(min(elements), max(elements) + 1):
		score = sum(abs(crab - position) for crab in elements)
		best_fuel_cost = min(best_fuel_cost, score)

	return best_fuel_cost


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [int(line) for line in f.readline().strip().split(',')]

	print('Day 07 : The Treachery of Whales - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
