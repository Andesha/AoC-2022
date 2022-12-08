with open('large.txt') as f:
    content = [list(map(int,line)) for line in f.read().splitlines()]

visible_count = 0
for y in range(1, len(content) - 1):
    for x in range(1, len(content[y]) - 1):
        max_height = content[y][x]
        if (max(content[y][:x]) < max_height or
            max(content[y][x+1:]) < max_height or
            max(row[x] for i, row in enumerate(content) if i < y) < max_height or 
            max(row[x] for i, row in enumerate(content) if i > y) < max_height 
           ):
            visible_count += 1

print('Part 1: ', (len(content)*4) - 4 + visible_count)