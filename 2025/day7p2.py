beams = {}
with open("day7input.txt", 'r') as file:
    for line in file:
        line = line.rstrip()
        if 'S' in line:
            beams[line.index('S')] = 1
            continue
        to_add = {}
        for c, char in enumerate(line):
            if char == '^' and c in beams:
                num_beams = beams.pop(c)
                if c > 0:
                    to_add[c - 1] = to_add.get(c - 1, 0) + num_beams
                if c < len(line) - 1:
                    to_add[c + 1] = to_add.get(c + 1, 0) + num_beams
        for i, num in to_add.items():
            beams[i] = beams.get(i, 0) + num

print(sum(beams.values()))