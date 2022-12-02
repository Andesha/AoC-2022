shape_val = {'X': 1, 'Y': 2, 'Z': 3}
win_dict = {
    'A': {'X': 3, 'Y': 6, 'Z': 0},
    'B': {'X': 0, 'Y': 3, 'Z': 6},
    'C': {'X': 6, 'Y': 0, 'Z': 3}
}
strat_dict = {
    'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'},
    'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
    'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'}
}

with open('large.txt') as f:
    p1_sum, p2_sum = 0, 0
    for l,r in [x.split() for x in f.read().splitlines()]:
        p1_sum += win_dict[l][r] + shape_val[r]
        p2_sum += shape_val[strat_dict[l][r]] + win_dict[l][strat_dict[l][r]]

print(f'Part 1: {p1_sum}\tPart 2: {p2_sum}')