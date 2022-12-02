# Part 1:
# A, B, C -> R, P, S
# X, Y, Z -> R, P, S
win_dict = {
    'A': {'X': 3, 'Y': 6, 'Z': 0},
    'B': {'X': 0, 'Y': 3, 'Z': 6},
    'C': {'X': 6, 'Y': 0, 'Z': 3}
}
shape_val = {'X': 1, 'Y': 2, 'Z': 3}

# Part 2:
# X, Y, Z -> L, D, W
strat_val = {'X': 0, 'Y': 3, 'Z': 6}
strat_dict = {
    'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'},
    'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
    'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'}
}

with open('large.txt') as f:
    pairs = [x.split() for x in f.read().splitlines()]

sum_val = 0
for l,r in pairs:
    sum_val += (win_dict[l][r] + shape_val[r])
print('Part 1: ', sum_val)

second_sum = 0
for l,r in pairs:
    second_sum += shape_val[strat_dict[l][r]] + strat_val[r]
print('Part 2: ', second_sum)