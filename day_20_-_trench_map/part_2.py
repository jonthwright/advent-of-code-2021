#!/usr/bin/env python3

import os


def build_index(input_image: list[str], x: int, y: int, step: int) -> int:
	index = 0

	for dy in range(y - 1, y + 2):
		for dx in range(x - 1, x + 2):
			index <<= 1

			if 0 <= dy < len(input_image) and 0 <= dx < len(input_image[dy]):
				index |= (input_image[dy][dx] == '#')
			else:
				index |= step % 2

	return index

def enhance_image(image_enhancement_algorithm: str, input_image: list[str]) -> list[str]:
	enhanced_image = input_image

	for step in range(50):
		enhanced_image = [''.join(image_enhancement_algorithm[build_index(enhanced_image, x, y, step)]
							for x in range(-1, len(enhanced_image[0]) + 1))
								for y in range(-1, len(enhanced_image) + 1)]

	return enhanced_image

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
