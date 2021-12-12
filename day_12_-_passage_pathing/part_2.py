#!/usr/bin/env python3

from collections import defaultdict

def count_cave_pathings(cave_system: list[tuple[str, str]],
                        current_cave: str = 'start',
                        small_cave_encountered: bool = False,
                        visited_cave: set[str] = set()) -> int:

	if current_cave == 'end':
		return 1
	if current_cave in visited_cave:
		if current_cave == 'start' or (current_cave.islower() and small_cave_encountered):
			return 0
		if current_cave.islower():
			small_cave_encountered = current_cave.islower()

	return sum(count_cave_pathings(cave_system, next_cave, small_cave_encountered, visited_cave | {current_cave}) 
	                      			for next_cave in cave_system[current_cave])

def solution(elements: list[tuple[str, str]]) -> int:
	graph = defaultdict(set)

	for start, end in elements:
		graph[start].add(end)
		graph[end].add(start)

	return count_cave_pathings(graph)


def main():
	with open('input_file.txt', 'r') as f:
		inputs = [tuple(row.strip().split('-')) for row in f.readlines()]
	print('Day 12 : Passage Pathing - part 2')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
 