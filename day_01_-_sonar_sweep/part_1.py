#!/usr/bin/env python3

def solution(elements):
    measurements_inc = 0
    for i in range(len(elements)):
        if elements[i] > elements[i - 1]:
            measurements_inc += 1
    return measurements_inc
        

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [int(line) for line in f.readlines()]
	print('Day 01 : Sonar Sweep - part 1')
	print(f'>>> Answer : {solution(inputs)}')