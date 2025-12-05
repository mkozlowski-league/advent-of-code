fresh_ranges = []
total_fresh = 0

reading_ranges = True
with open("day5input.txt", 'r') as file:
    for line in file:
        line = line.rstrip()
        if not line:
            reading_ranges = False
            continue
        elif reading_ranges:
            fresh_ranges.append(tuple(map(int, line.split('-'))))
            continue
        
        id = int(line)
        if any(id >= start and id <= end for start, end in fresh_ranges):
            total_fresh += 1

print(total_fresh)
