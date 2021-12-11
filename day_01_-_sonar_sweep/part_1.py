#!/usr/bin/env python3

def solution(elements: list[int]) -> int:
	return sum(elements[i - 1] < elements[i] for i in range(1, len(elements)))


def main():
	with open('input_file.txt', 'r') as f:
		inputs = [int(line.strip()) for line in f.readlines()]
	print('Day 01 : Sonar Sweep - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()