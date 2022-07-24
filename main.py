class Slot:
    def __init__(self, a, b):
        self.time = a
        self.index = b


input_file = open("input_files/10.in")
rows = input_file.read().strip().split('\n')
total_lifeguards = int(rows[0])
slotList = [0] * 2 * total_lifeguards
actual_max_time = 0
unique_time_list = [0] * total_lifeguards
last_time = 0
unique_time_set = set()

for lifeguard in range(total_lifeguards):
    shift_time = rows[lifeguard + 1].split(' ')
    slotList[2 * lifeguard] = Slot(int(shift_time[0]), lifeguard)
    slotList[2 * lifeguard + 1] = Slot(int(shift_time[1]), lifeguard)

slotList.sort(key=lambda state: state.time)

for slot in slotList:
    if len(unique_time_set) == 1:
        for loneitem in unique_time_set:
            unique_time_list[loneitem] += slot.time - last_time
    if len(unique_time_set) > 0:
        actual_max_time += slot.time - last_time
    if slot.index in unique_time_set:
        unique_time_set.remove(slot.index)
    else:
        unique_time_set.add(slot.index)
    last_time = slot.time

maximum_common_time = 0
for lifeguard_unique_time in unique_time_list:
    maximum_common_time = max(maximum_common_time, actual_max_time - lifeguard_unique_time)
print(maximum_common_time)
