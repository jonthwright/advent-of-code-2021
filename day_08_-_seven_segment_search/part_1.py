#!/usr/bin/env python3

def solution(elements: list[tuple[list[str], list[str]]]) -> int:
	signal_range_set = set(range(5, 7))
	return sum(len(out_signal) not in signal_range_set for _, out_signals in elements for out_signal in out_signals)

def main():
	with open('input_file.txt', 'r') as f:
		inputs = [tuple(split.split() for split in line.split('|')) for line in f.readlines()]
	print('Day 08 : Seven Segment Search - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
