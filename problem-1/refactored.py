with open('large.txt') as f:
    block_list = []
    for block in f.read().split('\n\n'):
        block_list.append(sum([int(i) for i in block.split('\n')]))
block_list.sort()
print('Part 1: ', block_list[-1], 'Part 2: ', sum(block_list[-3:]))