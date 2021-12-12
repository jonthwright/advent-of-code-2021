#!/usr/bin/env python3

import os
from collections import defaultdict


def count_cave_pathings(cave_system: list[tuple[str, str]],
						current_cave: str = 'start',
						visited_cave: set[str] = set()) -> int:

	if current_cave == 'end':
		return 1
	if current_cave in visited_cave and (current_cave == 'start' or current_cave.islower()):
		return 0

	return sum(count_cave_pathings(cave_system, next_cave, visited_cave | {current_cave})
									for next_cave in cave_system[current_cave])

def solution(elements: list[tuple[str, str]]) -> int:
	graph = defaultdict(set)

	for start, end in elements:
		graph[start].add(end)
		graph[end].add(start)

	return count_cave_pathings(graph)


def main():
	aoc_day_loc = os.path.dirname(__file__).replace('\\', '/')
	with open(f'{aoc_day_loc}/input_file.txt', 'r') as f:
		inputs = [tuple(row.strip().split('-')) for row in f.readlines()]
	print('Day 12 : Passage Pathing - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
