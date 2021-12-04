#!/usr/bin/env python3

from typing import Tuple

def solution(elements: list[Tuple[str, int]]) -> int:
	depth = horizontal = aim = 0
	for cmd, unit in elements:
		match cmd:
			case "down" : aim += unit
			case "up" : aim -= unit
			case "forward" :
				horizontal += unit
				depth += aim * unit
	return depth * horizontal


def main():
	with open('input_file.txt', 'r') as f:
		inputs = [line.split(" ") for line in f.readlines()]
		inputs = [(line[0], int(line[1])) for line in inputs]
	print('Day 02 : Dive! - part 2')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()