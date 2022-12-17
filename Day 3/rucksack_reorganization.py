input = open("input.txt", "r")

# Part One
priority_sum = 0

for line in input:
    line = line.replace("\n", "")

    first_compartment = set(line[:len(line)//2])
    second_compartment = set(line[(len(line)//2):])

    union_compartments = first_compartment.intersection(second_compartment)

    for i in union_compartments:
        if i.isupper():
            priority_sum += ord(i) - 38
        else:
            priority_sum += ord(i) - 96

print("Part One Answer:", priority_sum)

# Part Two
input.seek(0)

badge_char = ""
badge_list = ""
priority_sum = 0

for num, line in enumerate(input):
    line = line.replace("\n", "")

    if num % 3 == 0:
        badge_list += badge_char
        badge_char = line
    else:
        badge_char = "".join(list(set([i for i in line if i in badge_char])))

badge_list += badge_char

for i in badge_list:
    if i.isupper():
        priority_sum += ord(i) - 38
    else:
        priority_sum += ord(i) - 96

print("Part Two Answer:", priority_sum)

input.close()