input = open("input.txt", "r")

# Setting Up file system directory with corresponding sizes
directory_sizes = {}
curr_directory = "/"

for line in input:
    line = (line.replace("\n", "")).split(" ")
    if line[1] == "cd":
        if line[2] == "..":
            last_index = (curr_directory[::-1]).index("/")
            curr_directory = curr_directory[:len(curr_directory) - last_index - 1]
            last_index = (curr_directory[::-1]).index("/")
            curr_directory = curr_directory[:len(curr_directory) - last_index - 1] + "/"
        elif line[2] != "/":
            curr_directory += line[2] + "/"

        if directory_sizes.get(curr_directory, None) == None:
            directory_sizes[curr_directory] = 0

    elif line[0] != "$" and line[0] != "dir":
        directory_sizes[curr_directory] += int(line[0])

for k in directory_sizes.keys():
    for i in directory_sizes.keys():
        if (i != k and k in i):
            directory_sizes[k] += directory_sizes[i]

# Part One
total_size_less_than_100k = 0

for v in directory_sizes.values():
    if v <= 100_000:
        total_size_less_than_100k += v

print("Part One Answer:", total_size_less_than_100k)

# Part Two
smallest_dir_size_to_delete = directory_sizes["/"]

for k, v in directory_sizes.items():
    if (v >= 30_000_000 - (70_000_000 - directory_sizes["/"])):
        smallest_dir_size_to_delete = min(smallest_dir_size_to_delete, v)

print("Part Two Answer:", smallest_dir_size_to_delete)

input.close()