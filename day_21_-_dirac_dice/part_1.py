#!/usr/bin/env python3

import os


def solution(elements: tuple[int, int]) -> int:
	player_one_pos, player_two_pos = (elem - 1 for elem in elements)

	player_one_score = player_two_score = 0
	dice_rolls = 0 
 
	while player_one_score < 1000 and player_two_score < 1000:
		player_one_pos = (player_one_pos + (dice_rolls + 1) * 3 + 3) % 10
		player_one_score += player_one_pos + 1
		dice_rolls += 3

		if player_one_score < 1000:
			player_two_pos = (player_two_pos + (dice_rolls + 1) * 3 + 3) % 10
			player_two_score += player_two_pos + 1
			dice_rolls += 3

	return (player_one_score * (player_one_score <= player_two_score) + player_two_score * (player_two_score < player_one_score)) * dice_rolls


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = tuple(int(row.strip()[row.rfind(' '):]) for row in f.readlines())

	print('Day 21 : Dirac Dice - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
