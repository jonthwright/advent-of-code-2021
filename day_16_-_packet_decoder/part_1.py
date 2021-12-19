#!/usr/bin/env python3

import os


def parse_packets(packet: str) -> tuple[int,]:
	version = int(packet[:3], 2)
	packet_id = int(packet[3:6], 2)

	if packet_id == 4:
		sub_packet = packet[6:]
		while sub_packet[0] == '1':
			sub_packet = sub_packet[5:]
		return version, sub_packet[5:]

	if packet[6] == '0':
		packet_length = int(packet[7: 22], 2)
		sub_packet_remaining, packet = packet[22: 22 + packet_length], packet[22 + packet_length:]

		while sub_packet_remaining:
			sub_version, sub_packet_remaining = parse_packets(sub_packet_remaining)
			version += sub_version
	else:
		packet_count = int(packet[7: 18], 2)
		packet = packet[18:]

		for _ in range(packet_count):
			sub_version, packet = parse_packets(packet)
			version += sub_version

	return version, packet


def packet_hexidecimal_to_binary(packet_hex: str) -> str:
	return "".join(f"{int(c, 16):04b}" for c in packet_hex)

def solution(elements: str) -> int:
	version_sums, _ = parse_packets(packet_hexidecimal_to_binary(elements))
	return version_sums

def main():
	aoc_day_loc = os.path.dirname(__file__).replace('\\', '/')

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = f.readline().strip()

	print('Day 16 : Packet Decoder - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
