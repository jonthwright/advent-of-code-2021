#!/usr/bin/env python3

import os


def reorient(pos: tuple[int, int, int], axis1: int, sign1: int, axis2: int, sign2: int) -> tuple[int, int, int]:
	axis3 = 3 - (axis1 + axis2)
	sign3 = 1 if (((axis2 - axis1) % 3 == 1) ^ (sign1 != sign2)) else -1

	return (pos[axis1] * sign1, pos[axis2] * sign2, pos[axis3] * sign3)

def differences(poses: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
	return [(x1 - x0, y1 - y0, z1 - z0) for (x0, y0, z0), (x1, y1, z1) in zip (poses, poses[1:])]

def try_align(known_beacons: set[tuple[int, int, int]], unaligned_beacons: list[tuple[int, int, int]]):
	for axis in range(3):
		known_sorted = sorted(known_beacons, key = lambda pos: pos[axis])
		unaligned_beacons.sort(key = lambda pos: pos[axis])

		known_differences = differences(known_sorted)
		unaligned_differences = differences(unaligned_beacons)
		intersection = set(known_differences) & set(unaligned_differences)

		if intersection:
			difference = intersection.pop()

			kx, ky, kz = known_sorted[known_differences.index(difference)]
			ux, uy, uz = unaligned_beacons[unaligned_differences.index(difference)]
			ox, oy, oz = (ux - kx, uy - ky, uz - kz)

			moved = {(x - ox, y - oy, z - oz) for (x, y, z) in unaligned_beacons}
			matches = known_beacons & moved

			if len(matches) >= 12:
				return moved, (ox, oy, oz)

	return None, None

def try_orient_and_align(known_beacons: set[tuple[int, int, int]], readings: list[tuple[int, int]]) -> tuple[set[tuple[int, int, int]], tuple[int, int, int]] | tuple[None, None]:
	for axis1 in range(3):
		for sign1 in [1, -1]:
			for axis2 in {0, 1, 2} - {axis1}:
				for sign2 in [1, -1]:
					orientation = (axis1, sign1, axis2, sign2)
					unaligned_beacons = [reorient(reading, *orientation) for reading in readings]
					aligned_beacons, scanner_pos = try_align(known_beacons, unaligned_beacons)

					if aligned_beacons:
						return aligned_beacons, scanner_pos

	return None, None

def orient_all(known_beacons: set[tuple[int, int, int]], known_scanners: list[tuple[int, int, int]], unaligned_readings: list[list[tuple[int, int]]]) -> None:
	while unaligned_readings:
		progress = False
		for readings in unaligned_readings:
			beacons, scanner_pos = try_orient_and_align(known_beacons, readings)
			if beacons:
				unaligned_readings.remove(readings)
				known_beacons |= beacons
				known_scanners.append(scanner_pos)
				progress = True
		assert progress

def parse_input_scanners(elements: list[str]) -> list[list[tuple[int, int, int]]]:
	scanners = []

	for line in elements:
		if '---' in line:
			scanners.append([])
		elif line.strip():
			scanners[-1].append(tuple(int(values) for values in line.split(',')))

	return scanners

def solution(elements: list[str]) -> int:
	scanner_readings = parse_input_scanners(elements)
	known_scanners = [(0, 0, 0)]
	known_beacons = set(scanner_readings[0])
	unaligned_readings = scanner_readings[1:]

	orient_all(known_beacons, known_scanners, unaligned_readings)
	return len(known_beacons)


def main():
	aoc_day_loc = os.path.dirname(__file__).replace('\\', '/')

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [row.strip() for row in f.readlines()]

	print('Day 19 : Beacon Scanner - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
