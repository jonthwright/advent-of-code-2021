#!/usr/bin/env python3

import os
import re


Cubiod = tuple[str, tuple[int, int], tuple[int, int], tuple[int, int]]

def range_len(range: tuple[int, int]) -> int:
	start, end = range
	return end - start

def sub_range(this: tuple[int, int], other: tuple[int, int]) -> tuple[int, int]:
	this_min, this_max = this
	other_min, other_max = other

	return max(this_min, other_min), min(this_max, other_max)

def intersect(cuboid_1: Cubiod, cuboid_2: Cubiod) -> bool:
    if not(cuboid_1[1][0] <= cuboid_2[1][1] and cuboid_1[1][1] >= cuboid_2[1][0]):
        return False
 
    if not(cuboid_1[2][0] <= cuboid_2[2][1] and cuboid_1[2][1] >= cuboid_2[2][0]):
        return False
 
    if not(cuboid_1[3][0] <= cuboid_2[3][1] and cuboid_1[3][1] >= cuboid_2[3][0]):
        return False
 
    return True

def get_intersection(cuboid_1: Cubiod, cuboid_2: Cubiod) -> Cubiod:
	x_range = sub_range(cuboid_1[1], cuboid_2[1])
	y_range = sub_range(cuboid_1[2], cuboid_2[2])
	z_range = sub_range(cuboid_1[3], cuboid_2[3])
  
	if cuboid_1[0] == cuboid_2[0]:
		if cuboid_1[0] == 'on':
			return 'off', x_range, y_range, z_range
		else:
			return 'on', x_range, y_range, z_range
	elif cuboid_1[0] == 'on' and cuboid_2[0] == 'off':
		return 'on', x_range, y_range, z_range
	return 'off', x_range, y_range, z_range

def get_volume(cuboid: Cubiod) -> int:
	_, x, y, z = cuboid

	return (x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1)

def solution(elements: list[Cubiod]) -> int:
	cuboids = []
 
	for current_cuboid in elements: 
		intersections = [get_intersection(current_cuboid, other_cuboid) for other_cuboid in cuboids if intersect(current_cuboid, other_cuboid)]
		cuboids.extend(intersections)
 
		if current_cuboid[0] == 'on':
			cuboids.append(current_cuboid)
  
	return sum(get_volume(cuboid) * (1 if cuboid[0] == 'on' else -1) for cuboid in cuboids)


def parse_inputs(inputs: str) -> Cubiod:
	str_input, int_inputs = inputs.split(' ')
	int_inputs = list(int(input_ints) for input_ints in re.findall(r'(-?\d+)', int_inputs))
	grouped_int_inputs = tuple(tuple(int_inputs[i: i + 2]) for i in range(0, len(int_inputs), 2))

	return str_input, *grouped_int_inputs

def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [parse_inputs(row.strip()) for row in f.readlines()]

	print('Day 22 : Reactor Reboot - part 2')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
