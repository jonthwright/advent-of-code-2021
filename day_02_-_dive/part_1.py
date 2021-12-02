#!/usr/bin/env python3

def solution(elements):
    depth = horizontal = 0

    for op, unit in elements:
        match op:
            case "down" : depth += unit
            case "up" : depth -= unit
            case "forward" : horizontal += unit
    return depth * horizontal
        
        
if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [line.split(" ") for line in f.readlines()]
		inputs = [(line[0], int(line[1])) for line in inputs]
	print('Day 02 : Dive! - part 1')
	print(f'>>> Answer : {solution(inputs)}')