#!/usr/bin/env python3

import os


def safe_index(x: int, y: int, col: int, row: int) -> bool:
	return 0 <= y < row and 0 <= x < col

def build_index(input_image: list[str], x: int, y: int, step: int) -> int:
	row_num, col_num = len(input_image[0]), len(input_image)
	index = 0

	for dy in range(y - 1, y + 2):
		for dx in range(x - 1, x + 2):
			safe = safe_index(dx, dy, col_num, row_num)
			index <<= 1
			index |= ((input_image[dy * safe][dx * safe] == '#') * safe + (step % 2) * (not safe))

	return index

def enhance_image(image_enhancement_algorithm: str, enhancing_image: list[str]) -> list[str]:
	for step in range(2):
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

	print('Day 20 : Trench Map - part 1')
	print(f'>>> Answer : {solution(aux_inputs, main_inputs)}')

if __name__ == '__main__':
	main()
