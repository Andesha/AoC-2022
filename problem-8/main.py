from functools import reduce

with open('large.txt') as f:
    trees = [list(map(int,line)) for line in f.read().splitlines()]
trees_range = range(len(trees))

def tree_caster(j, i, y, x):
    count = 1
    while True:
        ty, tx = y + (j * count), x + (i * count) # step
        if (ty not in trees_range) or (tx not in trees_range):
            return True, count - 1 # -1 since you never actually "go" there
        elif (trees[ty][tx] >= trees[y][x]):
            return False, count # done, you went x
        count += 1

visible_count, best_tree = 0, 0
for y in trees_range:
    for x in trees_range:
        scenic, valid = 1, False # accum vars
        for move in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            mv, mc = tree_caster(*move, y, x)
            if not valid and mv: # if we haven't counted yet, and is valid
                visible_count += 1
            valid |= mv
            scenic *= mc
        best_tree = max(scenic, best_tree)

print('Part 1: ', visible_count, 'Part 2: ', best_tree)