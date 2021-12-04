#!/usr/bin/env python3

def solution(elements: list[int]) -> int:
	measurements_inc = 0
	for i in range(len(elements)):
		measurements_inc += sum(elements[i + 1: i + 4]) > sum(elements[i: i + 3])
	return measurements_inc

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [int(line) for line in f.readlines()]
	print('Day 01 : Sonar Sweep - part 2')
	print(f'>>> Answer : {solution(inputs)}')