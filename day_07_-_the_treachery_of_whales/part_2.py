#!/usr/bin/env python3

import os


def crab_sum(crab: int, position: int) -> int:
    delta = abs(crab - position)
    return (delta * (delta + 1)) // 2

def solution(elements: list[int]) -> int:
	best_fuel_cost = float('inf')

	for position in range(min(elements), max(elements) + 1):
		fuel_cost = sum(crab_sum(crab, position) for crab in elements)
		best_fuel_cost = min(best_fuel_cost, fuel_cost)

	return best_fuel_cost


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [int(line) for line in f.readline().strip().split(',')]

	print('Day 07 : The Treachery of Whales - part 2')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
