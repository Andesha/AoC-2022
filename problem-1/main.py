def part1(): # Original answer
    with open('large.txt') as f:
        max_val = -1
        for block in f.read().split('\n\n'):
            block_val = sum([int(i) for i in block.split('\n')])
            if max_val < block_val:
                max_val = block_val
    print('Part 1: ', max_val)

def part2(): # Original answer
    with open('large.txt') as f:
        block_list = []
        for block in f.read().split('\n\n'):
            block_list.append(sum([int(i) for i in block.split('\n')]))
    block_list.sort()

    print('Part 1: ', block_list[-1])
    print('Part 2: ', sum(block_list[-3:]))

if __name__ == "__main__":
    # part1()
    part2()