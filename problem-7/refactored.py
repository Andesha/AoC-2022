from collections import defaultdict
from itertools import accumulate

path_stack, size_map = [], defaultdict(int)

with open('large.txt') as f:
    for line in [x.split() for x in f.read().splitlines()]:
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
print('Part 2: ', min(x for x in size_map.values() if x > size_map['/'] - 40_000_000))