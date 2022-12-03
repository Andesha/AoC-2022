def part1():
    with open('large.txt') as f:
        content = f.read().splitlines()

    alpha_lookup = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    runner = 0
    for bag in content:
        left = set(bag[:len(bag)//2])
        right = set(bag[len(bag)//2:])

        runner += (alpha_lookup.index(left.intersection(right).pop()) + 1)

    print('Part 1: ', runner)

def part2():
    with open('large.txt') as f:
        content = f.read().splitlines()

    alpha_lookup = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    runner = 0
    for i in range(0, len(content), 3):
        badge = set(content[i+0]).intersection(set(content[i+1])).intersection(set(content[i+2]))
        runner += (alpha_lookup.index(badge.pop()) + 1)

    print(runner)

if __name__ == "__main__":
    # part1()
    part2()