#!/usr/bin/env python3

def flashing_octopi(octopi: list[list[int]]) -> int:
	flashing_octopus, flashed_octopus = [], []
	flashes = 0

	for y in range(len(octopi)):
		for x in range(len(octopi[y])):
			octopi[y][x] += 1
			if octopi[y][x] == 10:
				flashing_octopus.append((x, y))

	while flashing_octopus:
		flashes += 1
		x, y = flashing_octopus.pop()
		flashed_octopus.append((x, y))

		for j, i in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
			dx, dy = x + i, y + j

			if 0 <= dy < len(octopi) and 0 <= dx < len(octopi[dy]):
				if octopi[dy][dx] == 9:
					flashing_octopus.append((dx, dy))
				if octopi[dy][dx] < 10:
					octopi[dy][dx] += 1

	for x, y in flashed_octopus:
		octopi[y][x] = 0

	return flashes

def solution(elements: list[list[int]]) -> int:
	return sum(flashing_octopi(elements) for _ in range(100))


def main():
	with open('input_file.txt', 'r') as f:
		inputs = [[int(col) for col in row.strip()] for row in f.readlines()]
	print('Day 11 : Dumbo Octopus - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
 