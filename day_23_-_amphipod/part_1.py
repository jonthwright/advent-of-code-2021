#!/usr/bin/env python3


import os


def amphipod_room_location(amphipod: str) -> int:
	return (ord(amphipod) - ord('A') + 1) * 2 + 1

def stoppable_positions(amphipod_field: list[list[str]]) -> tuple[int, int, int, int, int, int, int]:
	return tuple(i for i in range(1, len(amphipod_field[0]) - 1) if i not in range(3, 10, 2))

def is_in_own_room(amphipod_field: list[list[str]], x: int, y: int) -> bool:
	if not get_amphipod(amphipod_field, x, y):
		return False
	if x != amphipod_room_location(amphipod_field[y][x]):
		return False
	
	return True

def room_completed(amphipod_field: list[list[str]], x: int) -> bool:
	for y in range(2, 4):
		if not is_in_own_room(amphipod_field, x, y):
			return False

	return True

def completed_rooms(amphipod_field: list[list[str]]) -> bool:
	return room_completed(amphipod_field, 3) and room_completed(amphipod_field, 5) and room_completed(amphipod_field, 7) and room_completed(amphipod_field, 9)

def get_amphipod(amphipod_field: list[list[str]], x: int, y: int) -> int:
	return amphipod_field[y][x] if (65 <= ord(amphipod_field[y][x]) < 69) else 0

def check_room_empty(amphipod_field: list[list[str]], x: int) -> bool:
	for y in range(2, 4):
		if amphipod_field[y][x] != '.':
			return False

	return True

def is_blocking_room(amphipod_field: list[list[str]], x: int, y: int) -> bool:
	for j in range(y + 1, 4):
		if get_amphipod(amphipod_field, x, j) and not is_in_own_room(amphipod_field, x, j):
			return True

	return False

def room_available(amphipod_field: list[list[str]], x: int, y: int) -> bool:
	if check_room_empty(amphipod_field, room := amphipod_room_location(amphipod_field[y][x])):
		return True

	for y in range(2, 4):
		if amphipod_field[y][room] != '.' and not is_in_own_room(amphipod_field, room, y):
			return False

	return True

def is_empty_path(amphipod_field: list[list[str]], x: int, target_x: int) -> bool:
	while x != target_x:
		x += -1 * (x > target_x) + 1 * (x < target_x)

		if amphipod_field[1][x] != '.':
			return False

	return True

def blocked_in_room(amphipod_field: list[list[str]], x: int, y: int) -> bool:
	if y < 3:
		return False

	return amphipod_field[y - 1][x] != '.'

def move_to_room(amphipod_field: list[list[str]], x: int) -> int:
	for y in range(3, 1, -1):
		if amphipod_field[y][x] == '.':
			return y

def is_movable(amphipod_field, x, y):
	return (not is_in_own_room(amphipod_field, x, y) or is_blocking_room(amphipod_field, x, y)) and not blocked_in_room(amphipod_field, x, y)

def move_cost(amphipod_field: list[list[str]], x: int, y: int, i: int, j: int) -> int:
	return ((y - 1) + abs(x - i) + (j - 1)) * 10 ** (ord(amphipod_field[y][x]) - ord('A'))

def move(amphipod_field: list[list[str]], x: int, y: int, i: int, j: int) -> tuple[list[list[str]], int]:
	new_amphipod_field = []

	for dy in range(len(amphipod_field)):
		new_amphipod_field.append([])
		for dx in range(len(amphipod_field[dy])):
			if dx == x and dy == y:
				new_amphipod_field[dy].append(amphipod_field[j][i])
			elif dx == i and dy == j:
				new_amphipod_field[dy].append(amphipod_field[y][x])
			else:
				new_amphipod_field[dy].append(amphipod_field[dy][dx])

	return new_amphipod_field, move_cost(amphipod_field, x, y, i, j)

def amphipod_field_cost(amphipod_field: list[list[str]],cache: dict[tuple[tuple[str]]] = {}) -> int:
	if (hashable_field := ''.join(''.join(spot for spot in row) for row in amphipod_field)) in cache:
		return cache[hashable_field]
	if completed_rooms(amphipod_field):
		return 0

	costs = []
 
	for y in range(1, len(amphipod_field)):
		for x in range(1, len(amphipod_field[y])):
			amphipod = get_amphipod(amphipod_field, x, y)
			if not amphipod:
				continue
			if is_movable(amphipod_field, x, y):
				amphipod_room = amphipod_room_location(amphipod)
				if room_available(amphipod_field, x, y) and is_empty_path(amphipod_field, x, amphipod_room):
					new_amphopod_field, cost = move(amphipod_field, x, y, amphipod_room, move_to_room(amphipod_field, amphipod_room))
					newer_cost = amphipod_field_cost(new_amphopod_field)
					if newer_cost >= 0:
						costs.append(cost + newer_cost)
				elif y > 1:
					for i in stoppable_positions(amphipod_field):
						if not is_empty_path(amphipod_field, x, i):
							continue
						new_amphopod_field, cost = move(amphipod_field, x, y, i, 1)
						newer_cost = amphipod_field_cost(new_amphopod_field)
						if newer_cost >= 0:
							costs.append(cost + newer_cost)

	cache[hashable_field] = min(costs) if costs else -1
	return cache[hashable_field]

def solution(elements: list[list[str]]) -> int:
	return amphipod_field_cost(elements)


if __name__ == '__main__':
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [line.strip('\n') for line in f.readlines()]

	print('Day 23 : Amphipod - part 1')
	print(f'>>> Answer : {solution(inputs)}')
