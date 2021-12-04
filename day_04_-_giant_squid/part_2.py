#!/usr/bin/env python3

class Bingo:
	def __init__(self, board_mtx: list[list[int]]) -> None:
		self.board_mtx = board_mtx
		self.marked_board_mtx = [[0 for _ in row] for row in board_mtx]
		self.bingoed = False
		
	def check_target(self, target: int) -> None:
		if self.bingoed:
			return

		for i, row in enumerate(self.board_mtx):
			for j, num in enumerate(row):
				if num == target:
					self.marked_board_mtx[i][j] = 1

		self.check_win()
	
	def check_win(self) -> None:
		row_bingoed = any(all(row) for row in self.marked_board_mtx)
		col_bingoed = any(all(col) for col in zip(*self.marked_board_mtx))

		self.bingoed = row_bingoed or col_bingoed 
	
	@property
	def current_board_sum(self):
		return sum(num for i, row in enumerate(self.board_mtx)
			 			for j, num in enumerate(row) 
						if not self.marked_board_mtx[i][j])


def solution(header: list[int], elements: list[list[int]]) -> int:
	bingo_boards = [Bingo(elements[i: i + 5]) for i in range(0, len(elements), 5)]

	last_board_bingoed_sum = last_target_bingoed = 0

	for target_num in header:
		for board in bingo_boards:
			if not board.bingoed:
				board.check_target(target_num)
				if board.bingoed:
					last_board_bingoed_sum = board.current_board_sum
					last_target_bingoed = target_num

	return last_board_bingoed_sum * last_target_bingoed


def main():
	with open('input_file.txt', 'r') as f:
		input_header = [int(num) for num in f.readline().split(',')]
		inputs_lines = [[int(num) for num in inputs.strip('\n').split(' ') if num] 
				  					for inputs in f.readlines() if inputs != '\n']

	print('Day 04 : Giant Squid - part 2')
	print(f'>>> Answer : {solution(input_header, inputs_lines)}')    

if __name__ == '__main__':
	main()
