#!/usr/bin/env python3

import os


def is_within_boundary(x: int, y: int, cols: int, rows: int) -> bool:
	return 0 <= y < rows and 0 <= x < cols

def build_index(input_image: list[str], x: int, y: int, step: int) -> int:
	rows, cols = len(input_image), len(input_image[0])
	idx = 0

	for dy in range(y - 1, y + 2):
		for dx in range(x - 1, x + 2):
			safe_idx = is_within_boundary(dx, dy, cols, rows)
			idx <<= 1
			idx |= ((input_image[dy * safe_idx][dx * safe_idx] == '#') * safe_idx + (step % 2) * (not safe_idx))

	return idx

def enhance_image(image_enhancement_algorithm: str, enhancing_image: list[str]) -> list[str]:
	for step in range(50):
		enhancing_image = [''.join(image_enhancement_algorithm[build_index(enhancing_image, x, y, step)]
							for x in range(-1, len(enhancing_image[0]) + 1)) for y in range(-1, len(enhancing_image) + 1)]
	return enhancing_image

def solution(aux_element: str, main_elements: list[str]) -> int:
	enhanced_image = enhance_image(aux_element, main_elements)
	return sum(pixel == '#' for pixel_row in enhanced_image for pixel in pixel_row)


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		aux_inputs = f.readline().strip()
		f.readline()
		main_inputs = [row.strip() for row in f.readlines()]

	print('Day 20 : Trench Map - part 2')
	print(f'>>> Answer : {solution(aux_inputs, main_inputs)}')

if __name__ == '__main__':
	main()