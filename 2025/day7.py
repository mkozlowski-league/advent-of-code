beams = set()
num_splits = 0
with open("day7input.txt", 'r') as file:
    for line in file:
        line = line.rstrip()
        if 'S' in line:
            beams.add(line.index('S'))
        for c, char in enumerate(line):
            if char == '^' and c in beams:
                num_splits += 1
                beams.remove(c)
                if c > 0:
                    beams.add(c - 1)
                if c < len(line) - 1:
                    beams.add(c + 1)

print(num_splits)