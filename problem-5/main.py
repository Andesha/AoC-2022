import re
from collections import defaultdict
p1_stacks = defaultdict(list) # Pre-allocate items in dict with list
p2_stacks = defaultdict(list)

with open('large.txt') as f:
    puzzle, moves = f.read().split('\n\n')
# Transpose for line reading
puzzle = list(map(list, zip(*puzzle.splitlines())))
for row in puzzle:
    if any(char.isdigit() for char in row): # Valid row
        swap = row[::-1] # Index at head now
        for item in swap[1:]:
            if item.strip(): # Falsey; if true valid to append
                p1_stacks[swap[0]].append(item)
                p2_stacks[swap[0]].append(item)

for move in moves.splitlines():
    instructions = re.findall(r'\d+', move) # many, from, to

    count = 0 # Crane 9000; (read -> pop) * n
    while count < int(instructions[0]):
        p1_stacks[instructions[2]].append(p1_stacks[instructions[1]][-1])
        p1_stacks[instructions[1]].pop()
        count += 1

    move_buffer = [] # Crane 9001; (read * n) -> reverse -> push
    for _ in range(int(instructions[0])):
        move_buffer.append(p2_stacks[instructions[1]].pop())
    p2_stacks[instructions[2]].extend(move_buffer[::-1])

print(f"Part 1: {''.join(v[-1] for _,v in p1_stacks.items())}")
print(f"Part 2: {''.join(v[-1] for _,v in p2_stacks.items())}")