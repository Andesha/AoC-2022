from collections import defaultdict
from itertools import accumulate

with open('large.txt') as f:
    content = [x.split() for x in f.read().splitlines()]

path_stack = []
size_map = defaultdict(int)

for line in content:
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '..':
                path_stack.pop()
            else:
                path_stack.append(line[2])
    else:
        if line[0].isnumeric(): # Only do work if addition to do
            for p in accumulate(path_stack): # Generates powerset!
                size_map[p] += int(line[0])

print('Part 1: ', sum(x for x in size_map.values() if x < 100_000))
min_val = 100_000_000
for k in size_map.keys():
    if size_map['/'] - size_map[k] + 30_000_000 < 70_000_000:
        if size_map[k] < min_val:
            min_val = size_map[k]
print('Part 2: ', min_val)