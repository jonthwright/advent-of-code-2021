#!/usr/bin/env python3

import os
import numpy as np
from math import prod

OPCODE = {
	0: sum,
	1: prod,
	2: min,
	3: max,
	5: lambda subs: subs[0] > subs[1],
	6: lambda subs: subs[0] < subs[1],
	7: lambda subs: subs[0] == subs[1]
}

def parse_packets(packet: str) -> str:
	packet_id = int(packet[3:6], 2)
	sub_packets = []

	if packet_id == 4:
		packet_value = 0
		sub_packet = packet[6:]

		while True:
			packet_value <<= 4
			packet_value |= int(sub_packet[1: 5], 2)

			if sub_packet[0] == '0':
				return packet_value, sub_packet[5:]

			sub_packet = sub_packet[5:]

	if packet[6] == '0':
		packet_length = int(packet[7: 22], 2)
		sub_packet_remaining, packet = packet[22: 22 + packet_length], packet[22 + packet_length:]

		while sub_packet_remaining:
			sub_packet, sub_packet_remaining = parse_packets(sub_packet_remaining)
			sub_packets.append(sub_packet)
	else:
		packet_count = int(packet[7: 18], 2)
		packet = packet[18:]

		for _ in range(packet_count):
			sub_packet, packet = parse_packets(packet)
			sub_packets.append(sub_packet)

	return OPCODE[packet_id](sub_packets), packet


def packet_hexidecimal_to_binary(packet_hex: str) -> str:
	return "".join(f"{int(c, 16):04b}" for c in packet_hex)

def solution(elements: str) -> int:
	decoded_packets, _ = parse_packets(packet_hexidecimal_to_binary(elements))
	return decoded_packets

def main():
	aoc_day_loc = os.path.dirname(__file__).replace('\\', '/')

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = f.readline().strip()

	print('Day 16 : Packet Decoder - part 2')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
