input = open("input.txt", "r")

# Part One
overlaps = 0

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

for line in input:
    line = line.replace("\n", "")
    pairs = line.split(",")
    assignment_pairs = [i.split("-") for i in pairs]

    fnum_first_assignment = int(assignment_pairs[0][0])
    snum_first_assignment = int(assignment_pairs[0][1])
    fnum_second_assignment = int(assignment_pairs[1][0])
    snum_second_assignment = int(assignment_pairs[1][1])

    # Swap values to order processes
    if fnum_first_assignment > fnum_second_assignment:
        fnum_first_assignment, fnum_second_assignment = swap(fnum_first_assignment, fnum_second_assignment)
        snum_first_assignment, snum_second_assignment = swap(snum_first_assignment, snum_second_assignment)
    
    if fnum_first_assignment == fnum_second_assignment:
        if snum_first_assignment < snum_second_assignment:
            fnum_first_assignment, fnum_second_assignment = swap(fnum_first_assignment, fnum_second_assignment)
            snum_first_assignment, snum_second_assignment = swap(snum_first_assignment, snum_second_assignment)
    
    if fnum_second_assignment <= snum_first_assignment and snum_second_assignment <= snum_first_assignment:
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

    # Swap values to order processes
    if fnum_first_assignment > fnum_second_assignment:
        fnum_first_assignment, fnum_second_assignment = swap(fnum_first_assignment, fnum_second_assignment)
        snum_first_assignment, snum_second_assignment = swap(snum_first_assignment, snum_second_assignment)
    
    if fnum_first_assignment == fnum_second_assignment:
        if snum_first_assignment < snum_second_assignment:
            fnum_first_assignment, fnum_second_assignment = swap(fnum_first_assignment, fnum_second_assignment)
            snum_first_assignment, snum_second_assignment = swap(snum_first_assignment, snum_second_assignment)
    
    if fnum_second_assignment <= snum_first_assignment:
        overlaps += 1

print("Part Two Answer:", overlaps)

input.close()