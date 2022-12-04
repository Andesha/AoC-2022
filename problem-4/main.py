with open('large.txt') as f:
    content = [x.split(',') for x in f.read().splitlines()]

p1_count = p2_count = 0
for left,right in content:
    ls = [int(x) for x in left.split('-')]
    rs = [int(x) for x in right.split('-')]
    left_set = set(range(ls[0],ls[1]+1))
    right_set = set(range(rs[0],rs[1]+1))

    if left_set.issubset(right_set) or right_set.issubset(left_set):
        p1_count += 1

    if len(left_set & right_set):
        p2_count += 1

print(p1_count)
print(p2_count)