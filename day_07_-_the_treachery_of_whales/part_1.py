#!/usr/bin/env python3

import functools

def solution(elements: list[int]) -> int:
	best_fuel_cost = float('inf')

	for position in range(min(elements), max(elements) + 1):
		score = functools.reduce(lambda acc, crab: acc + abs(crab - position), elements, 0)
		best_fuel_cost = min(best_fuel_cost, score)

	return best_fuel_cost


def main():
	with open('input_file.txt', 'r') as f:
		inputs = [int(line) for line in f.readline().split(',')]
	print('Day 07 : The Treachery of Whales - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
