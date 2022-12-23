input = open("input.txt", "r")

tree_grid = []

# Setting up tree grid
for line in input:
    line = line.replace("\n", "")
    tree_line = []
    for i in line:
        tree_line.append(int(i))
    tree_grid.append(tree_line)

if len(tree_grid) <= 0:
    exit()

# Part One
num_visible = 0
    
# Visible inner trees
for i in range(1, len(tree_grid) - 1):
    for j in range(1, len(tree_grid[i]) - 1):

        is_visible_top = tree_grid[i][j] > max([tree_grid[x][j] for x in range(0, i)])
        is_visible_bottom = tree_grid[i][j] > max([tree_grid[x][j] for x in range(i+1, len(tree_grid))])
        is_visible_left = tree_grid[i][j] > max([tree_grid[i][x] for x in range(0, j)])
        is_visible_right = tree_grid[i][j] > max([tree_grid[i][x] for x in range(j+1, len(tree_grid[i]))])

        if is_visible_top or is_visible_bottom or is_visible_left or is_visible_right:
            num_visible += 1

# Visible outer trees
num_visible += (len(tree_grid) * 2) + ((len(tree_grid[0]) - 2) * 2)

print("Part One Answer:", num_visible)

# Part Two
max_scenic_score = 0

# Visible trees
for i in range(len(tree_grid)):
    for j in range(len(tree_grid[i])):

        num_visible_top = 0
        for x in range(i, -1, -1):
            if i == x:
                continue
            if tree_grid[i][j] > tree_grid[x][j]:
                num_visible_top += 1
            else:
                num_visible_top += 1
                break

        num_visible_bottom = 0
        for x in range(i, len(tree_grid)):
            if i == x:
                continue
            if tree_grid[i][j] > tree_grid[x][j]:
                num_visible_bottom += 1
            else:
                num_visible_bottom += 1
                break

        num_visible_left = 0
        for x in range(j, -1, -1):
            if j == x:
                continue
            if tree_grid[i][j] > tree_grid[i][x]:
                num_visible_left += 1
            else:
                num_visible_left += 1
                break

        num_visible_right = 0
        for x in range(j, len(tree_grid)):
            if j == x:
                continue
            if tree_grid[i][j] > tree_grid[i][x]:
                num_visible_right += 1
            else:
                num_visible_right += 1
                break
        
        curr_scenic_score = num_visible_top * num_visible_bottom * num_visible_left * num_visible_right
        max_scenic_score = max(max_scenic_score, curr_scenic_score)

print("Part Two Answer:", max_scenic_score)

input.close()