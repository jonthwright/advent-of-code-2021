#!/usr/bin/env python3

import functools

def solution(elements: list[int]) -> int:
	size = len(elements)
	gamma_rate = 0
	max_bit_length = max(elements).bit_length()

	for offset in range(max_bit_length, -1, -1):
		ones_counter = functools.reduce(lambda x, y: x + ((y >> offset) & 1), elements, 0)
		gamma_rate |= (ones_counter > (size // 2)) << offset
	
	epsilon_rate = gamma_rate ^ (2 ** max_bit_length - 1)
 
	return gamma_rate * epsilon_rate


def main():
	with open('input_file.txt', 'r') as f:
		inputs = [int(line, 2) for line in f.readlines()]
	print('Day 03 : Binnary Diagnostics - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()