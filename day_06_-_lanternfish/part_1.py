#!/usr/bin/env python3

from collections import defaultdict, Counter

def solution(elements: list[int]) -> int:
	lanternfish_school = Counter(elements)

	for _ in range(80):
		new_lanternfish_school = defaultdict(int)
		for lantern_timer, latern_count in lanternfish_school.items():
			if lantern_timer > 0:
				new_lanternfish_school[lantern_timer - 1] += latern_count 
			else:
				new_lanternfish_school[6] += latern_count
				new_lanternfish_school[8] += latern_count 
		lanternfish_school = new_lanternfish_school

	return sum(lanternfish_school.values())


def main():
	with open('input_file.txt', 'r') as f:
		inputs = [int(line) for line in f.readline().split(',')]
	print('Day 06 : Lanternfish - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
