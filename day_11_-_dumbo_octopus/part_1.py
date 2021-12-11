#!/usr/bin/env python3


def flashing_octopi(octopi: list[list[int]]) -> int:
	flashing_octopus, flashed_octopus = [], []
	flashes = 0

	for y in range(len(octopi)):
		for x in range(len(octopi[y])):
			octopi[y][x] += 1
			if octopi[y][x] == 10:
				flashing_octopus.append((y, x))

	while flashing_octopus:
		flashes += 1
		y, x = flashing_octopus.pop()
		flashed_octopus.append((y, x))

		for j, i in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
			dy, dx = y + j, x + i

			if 0 <= dy < len(octopi) and 0 <= dx < len(octopi[dy]):
				if octopi[dy][dx] == 9:
					flashing_octopus.append((dy, dx))
				if octopi[dy][dx] < 10:
					octopi[dy][dx] += 1

	for y, x in flashed_octopus:
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
 