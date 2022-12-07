length = 14 # Change to 4 for p1
with open('large.txt') as f:
    whole_packet = f.read()
    for i in range(length, len(whole_packet)):
        if len(set(whole_packet[i-length:i])) == length:
            print(f'Found marker "{whole_packet[i-length:i]}" at pos: {i}') # same as above change
            break