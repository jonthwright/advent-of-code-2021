#!/usr/bin/env python3

import os


def flashing_octopi(octopi: list[list[int]]) -> int:
	flashing_octopus, flashed_octopus = [], set()
	flashes = 0

	for y in range(len(octopi)):
		for x in range(len(octopi[y])):
			octopi[y][x] += 1
			if octopi[y][x] == 10:
				flashing_octopus.append((x, y))

	while flashing_octopus:
		flashes += 1
		x, y = flashing_octopus.pop()
		flashed_octopus.add((x, y))

		for dy in range(-1, 2):
			dy += y
			for dx in range(-1, 2):
				dx += x

				if 0 <= dy < len(octopi) and 0 <= dx < len(octopi[dy]) and (dx, dy) not in flashed_octopus:
					if octopi[dy][dx] == 9:
						flashing_octopus.append((dx, dy))
					octopi[dy][dx] += 1

	for x, y in flashed_octopus:
		octopi[y][x] = 0

	return flashes

def solution(elements: list[list[int]]) -> int:
	return sum(flashing_octopi(elements) for _ in range(100))


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [[int(col) for col in row.strip()] for row in f.readlines()]

	print('Day 11 : Dumbo Octopus - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
 