from typing import List

input_file = open('1.in')
rows = input_file.read().strip().split('\n')
total_lifeguards = int(rows[0])

lifeguards_shift_list: List[List[int]] = list()  # declaring list of list in python3
for lifeguard in range(total_lifeguards):
	shift_slots = rows[lifeguard + 1].split(' ')
	shift_slots_list = list(map(int, shift_slots))
	lifeguards_shift_list.append(shift_slots_list)

print(lifeguards_shift_list)
