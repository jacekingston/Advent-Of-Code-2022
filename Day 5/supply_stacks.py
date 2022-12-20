input = open("input.txt", "r")

def set_stacks(input):
    stack = {}
    
    # Parsing crate stacks
    for line in input:
        line = line.replace("\n", "")
        stack_string = ""

        for i in range(len(line)):
            if i % 4 == 1 and line[i] != "":
                stack_string += line[i]

        for i in range(len(stack_string)):
            if stack.get(i+1, None) == None:
                stack[i+1] = []
                
        for i in range(len(stack_string)):
            stack[i+1].append(stack_string[i])
        
        if line == "":
            for k, v in stack.items():
                v[:] = reversed([crate for crate in v if crate != ' '])
                v.remove(str(k))
            break

    return stack

# Part One
stacks = set_stacks(input)

# Moving crates
for line in input:
    line = line.replace("\n", "")
    
    line = line.replace("move ", "").replace(" from ", " ").replace(" to ", " ")
    moves = line.split(" ")
    moves = [int(i) for i in moves]
    
    for i in range(moves[0]):
        stacks[moves[2]].append(stacks[moves[1]].pop())

print("Part One Answer:", "".join([v[len(v)-1] for v in stacks.values()]))

# Part Two
input.seek(0)
stacks = set_stacks(input)

for line in input:
    line = line.replace("\n", "")
    line = line.replace("move ", "").replace(" from ", " ").replace(" to ", " ")
    moves = line.split(" ")
    moves = [int(i) for i in moves]
    
    stacks[moves[2]] += stacks[moves[1]][len(stacks[moves[1]])-moves[0]:]
    stacks[moves[1]] = stacks[moves[1]][:len(stacks[moves[1]])-moves[0]]

print("Part Two Answer:", "".join([v[len(v)-1] for v in stacks.values()]))