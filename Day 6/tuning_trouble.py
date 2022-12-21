input = open("input.txt", "r")
line = input.read()

def get_unique_substring(length):
    last_data_stream_packet = 0
    for i in range(len(line) - length):
        if len(set(line[i:i+length])) == length:
            last_data_stream_packet = i + length
            break
    return last_data_stream_packet

# Part One
print("Part One Answer:", get_unique_substring(4))

# Part Two
print("Part Two Answer:", get_unique_substring(14))

input.close()