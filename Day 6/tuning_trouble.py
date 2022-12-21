input = open("input.txt", "r")
line = input.read()

# Part One
last_data_stream_packet = 0

for i in range(len(line) - 4):
    if len(set(line[i:i+4])) == 4:
        last_data_stream_packet = i + 4
        break

print("Part One Answer:", last_data_stream_packet)

# Part Two
for i in range(len(line) - 14):
    if len(set(line[i:i+14])) == 14:
        last_data_stream_packet = i + 14
        break

print("Part Two Answer:", last_data_stream_packet)

input.close()