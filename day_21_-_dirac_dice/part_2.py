#!/usr/bin/env python3

import os
from collections import defaultdict


def solution(elements: tuple[int, int]) -> int:
	player_one_pos, player_two_pos = (elem - 1 for elem in elements)

	player_one_wins = player_two_wins = 0
	quantum_die_rolls = tuple(sum((x, y, z)) for z in (1, 2, 3) for y in (1, 2, 3) for x in (1, 2, 3))
 
	universes = defaultdict(int)
	universes[(player_one_pos, player_two_pos, 0, 0)] = 1

	while len(universes) > 0:
		new_universes = defaultdict(int)
		for current_universe in universes:
			for n in quantum_die_rolls:
				new_pos = (current_universe[0] + n) % 10
				new_score = current_universe[2] + new_pos + 1

				if new_score >= 21:
					player_one_wins += universes[current_universe]
				else:
					new_universes[(new_pos, current_universe[1], new_score, current_universe[3])] += universes[current_universe]
		universes = new_universes

		new_universes = defaultdict(int)
		for current_universe in universes:
			for n in quantum_die_rolls:
				new_pos = (current_universe[1] + n) % 10
				new_score = current_universe[3] + new_pos + 1

				if new_score >= 21:
					player_two_wins += universes[current_universe]
				else:
					new_universes[(current_universe[0], new_pos, current_universe[2], new_score)] += universes[current_universe]
		universes = new_universes

	return player_one_wins * (player_one_wins >= player_two_wins) + player_two_wins * (player_two_wins > player_one_wins)

def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = tuple(int(row.strip()[row.rfind(' '):]) for row in f.readlines())

	print('Day 21 : Dirac Dice - part 2')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
