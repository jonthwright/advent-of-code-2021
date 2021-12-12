#!/usr/bin/env python3

import os


def solution(elements: list[tuple[list[str], list[str]]]) -> int:
	signal_summation = 0
 
	for in_signals, out_signals in elements:
		in_signal_dict = {len(in_signal) : set(in_signal) for in_signal in in_signals}

		for unit, out_signal in enumerate(map(set, out_signals)):
			unit_multiplier = 10 ** (3 - unit)
			match len(out_signal), len(out_signal & in_signal_dict[2]), len(out_signal & in_signal_dict[4]):
				case 2, _, _: signal_summation += 1 * unit_multiplier
				case 3, _, _: signal_summation += 7 * unit_multiplier
				case 4, _, _: signal_summation += 4 * unit_multiplier
				case 7, _, _: signal_summation += 8 * unit_multiplier
				case 5, 1, 2: signal_summation += 2 * unit_multiplier
				case 5, 1, 3: signal_summation += 5 * unit_multiplier
				case 5, 2, _: signal_summation += 3 * unit_multiplier
				case 6, 1, 3: signal_summation += 6 * unit_multiplier
				case 6, 2, 4: signal_summation += 9 * unit_multiplier
	
	return signal_summation


def main():
	aoc_day_loc = os.path.dirname(__file__).replace('\\', '/')
	with open(f'{aoc_day_loc}/input_file.txt', 'r') as f:
		inputs = [tuple(split.split() for split in line.strip().split('|')) for line in f.readlines()]
	print('Day 08 : Seven Segment Search - part 2')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
