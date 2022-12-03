alpha_lookup = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
p1_sum = p2_sum = 0

with open('large.txt') as f:
    content = f.read().splitlines()

for bag in content:
    both = set(bag[:len(bag)//2]).intersection(set(bag[len(bag)//2:]))
    p1_sum += (alpha_lookup.index(both.pop()) + 1)

for i in range(0, len(content), 3):
    badge = set(content[i+0]).intersection(set(content[i+1])) \
        .intersection(set(content[i+2]))
    p2_sum += (alpha_lookup.index(badge.pop()) + 1)

print(f'Part 1: {p1_sum}\tPart 2: {p2_sum}')