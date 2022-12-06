with open('large.txt') as f:
    for packet in f.read().splitlines():
        for i in range(0, len(packet)-3):
            marker = [packet[i+x] for x in range(14)] # literally just changed this from 4 to 14 for p1 to p2
            if len(marker) == len(set(marker)):
                print(f'Found marker "{marker}" at pos: {i+14}') # same as above change
                break