input = open("input.txt", "r")

# Part One
overlaps = 0

for line in input:
    line = line.replace("\n", "")
    pairs = line.split(",")
    assignment_pairs = [i.split("-") for i in pairs]

    fnum_first_assignment = int(assignment_pairs[0][0])
    snum_first_assignment = int(assignment_pairs[0][1])
    fnum_second_assignment = int(assignment_pairs[1][0])
    snum_second_assignment = int(assignment_pairs[1][1])

    if (fnum_first_assignment <= fnum_second_assignment and snum_first_assignment >= snum_second_assignment) or (fnum_first_assignment >= fnum_second_assignment and snum_first_assignment <= snum_second_assignment):
        overlaps += 1

print("Part One Answer:", overlaps)

# Part Two
input.seek(0)

overlaps = 0

for line in input:
    line = line.replace("\n", "")
    pairs = line.split(",")
    assignment_pairs = [i.split("-") for i in pairs]

    fnum_first_assignment = int(assignment_pairs[0][0])
    snum_first_assignment = int(assignment_pairs[0][1])
    fnum_second_assignment = int(assignment_pairs[1][0])
    snum_second_assignment = int(assignment_pairs[1][1])

    if (fnum_first_assignment <= snum_second_assignment and snum_first_assignment >= fnum_second_assignment):
        overlaps += 1

print("Part Two Answer:", overlaps)

input.close()