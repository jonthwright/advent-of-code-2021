#!/usr/bin/env python3

from typing import Iterator

class Bingo:
	def __init__(self, board_mtx: list[list[int]]) -> None:
		self.__board_mtx = board_mtx
		self.__marked_board_mtx = [[0 for _ in row] for row in board_mtx]
		
	def mark_drawn_number(self, target: int) -> None:
		for i, row in enumerate(self.__board_mtx):
			for j, num in enumerate(row):
				if num == target:
					self.__marked_board_mtx[i][j] = 1
	
	@property
	def is_winning_board(self) -> bool:
		row_bingoed = any(all(row) for row in self.__marked_board_mtx)
		col_bingoed = any(all(col) for col in zip(*self.__marked_board_mtx))

		return row_bingoed or col_bingoed 
	
	def __iter__ (self) -> Iterator[int]:
		for row in range(len(self.__board_mtx)):
			for col in range(len(self.__board_mtx[row])):
				if not self.__marked_board_mtx[row][col]:
					yield self.__board_mtx[row][col]


def solution(header: list[int], elements: list[list[int]]) -> int:
	bingo_boards = [Bingo(elements[i: i + 5]) for i in range(0, len(elements), 5)]

	for target_num in header:
		for board in bingo_boards:
			board.mark_drawn_number(target_num)
			if board.is_winning_board:
				return sum(board) * target_num

	return -1


def main():
	with open('input_file.txt', 'r') as f:
		input_header = [int(num) for num in f.readline().split(',')]
		inputs_lines = [[int(num) for num in inputs.strip('\n').split(' ') if num] 
                  					for inputs in f.readlines() if inputs != '\n']

	print('Day 04 : Giant Squid - part 1')
	print(f'>>> Answer : {solution(input_header, inputs_lines)}')

if __name__ == '__main__':
	main()