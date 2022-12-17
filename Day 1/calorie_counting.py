input = open("input.txt", "r")

max_calories = 0
curr_calories = 0

# Part 1
for line in input:
    if line != "\n":
        curr_calories += int(line)
        max_calories = max(curr_calories, max_calories)
    else:
        curr_calories = 0

print("Part One Answer:", max_calories)

# Part 2
input.seek(0)

top_three = [0, 0, 0]

curr_calories = 0

for line in input:
    if line != "\n":
        curr_calories += int(line)
        for i in range(len(top_three)):
            if curr_calories > top_three[i]:
                top_three[i] = curr_calories
                break
        top_three.sort()
    else:
        curr_calories = 0

print("Part Two Answer:", sum(top_three))

input.close()