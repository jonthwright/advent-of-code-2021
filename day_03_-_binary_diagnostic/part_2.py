#!/usr/bin/env python3

import functools

def solution(elements: list[int]) -> int:
	max_bit_length = max(elements).bit_length()
	oxygen_rating = carbon_dioxide_rating = elements.copy()
 
	for offset in range(max_bit_length - 1, -1, -1):
		if len(oxygen_rating) > 1:
			ones_oxygen = functools.reduce(lambda x, y: x + ((y >> offset) & 1), oxygen_rating, 0)
			zeroes_oxygen = len(oxygen_rating) - ones_oxygen

			if zeroes_oxygen <= ones_oxygen:
				oxygen_rating = [o for o in oxygen_rating if o & (1 << offset)]
			else:
				oxygen_rating = [o for o in oxygen_rating if not (o & (1 << offset))]

		if len(carbon_dioxide_rating) > 1:
			ones_carbon_dioxide = functools.reduce(lambda x, y: x + ((y >> offset) & 1), carbon_dioxide_rating, 0)
			zeroes_carbon_dioxide = len(carbon_dioxide_rating) - ones_carbon_dioxide

			if zeroes_carbon_dioxide <= ones_carbon_dioxide:
				carbon_dioxide_rating = [co2 for co2 in carbon_dioxide_rating if not (co2 & (1 << offset))]
			else:
				carbon_dioxide_rating = [co2 for co2 in carbon_dioxide_rating if co2 & (1 << offset)]

	return oxygen_rating[0] * carbon_dioxide_rating[0]


def main():
	with open('input_file.txt', 'r') as f:
		inputs = [int(line.strip(), 2) for line in f.readlines()]
	print('Day 03 : Binary Diagnostics - part 2')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()