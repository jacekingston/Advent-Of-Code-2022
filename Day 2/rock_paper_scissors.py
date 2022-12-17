input = open("input.txt", "r")

total_score = 0

# Part One
opponent_moves = ["A", "B", "C"]
elf_moves = ["X", "Y", "Z"]

for line in input:

    game = line.split(" ")
    game[1] = game[1].replace("\n", "")

    opponent_choice = opponent_moves.index(game[0])
    elf_choice = elf_moves.index(game[1])

    if (elf_choice == (opponent_choice + 1) % 3): # Elf Win
        total_score += elf_choice + 6 + 1
    elif (elf_choice == (opponent_choice + 2) % 3): # Elf Loss
        total_score += elf_choice + 1
    else: # Tie Game
        total_score += elf_choice + 3 + 1

print("Part One Answer:", total_score)

# Part 2
input.seek(0)

total_score = 0

for line in input:

    game = line.split(" ")
    game[1] = game[1].replace("\n", "")

    opponent_choice = opponent_moves.index(game[0])

    if game[1] == "X": # Elf Loss
        total_score += ((opponent_choice + 2) % 3) + 1
    elif game[1] == "Y": # Tie Game
        total_score += opponent_choice + 3 + 1
    else: # Tie Game
        total_score += ((opponent_choice + 1) % 3) + 6 + 1

print("Part Two Answer:", total_score)

input.close()