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
        ub, uc = tree_caster(1, 0, y, x)  # up
        db, dc = tree_caster(-1, 0, y, x) # down
        lb, lc = tree_caster(0, -1, y, x) # left
        rb, rc = tree_caster(0, 1, y, x)  # right

        if any([ub, db, rb, lb]):
            visible_count += 1
        best_tree = max(reduce(lambda x, y: x * y, [uc, dc, rc, lc]), best_tree)

print('Part 1: ', visible_count, 'Part 2: ', best_tree)