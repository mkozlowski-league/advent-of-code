def add_range(start, end, ranges):
    for i, (s, e) in enumerate(ranges):
        # Extend to the right
        if s <= start <= e and end >= e:
            ranges[i] = (s, end)
            break
        # Extend to the left
        elif start <= s and s <= end <= e:
            ranges[i] = (start, e)
            break
        # Extend on both sides
        elif start <= s and end >= e:
            ranges[i] = (start, end)
            break
        # Completely contained
        elif s <= start and end <= e:
            break

    else:
        ranges.append((start, end))
    
    return ranges

fresh_ranges = []
with open("day5input.txt", 'r') as file:
    for line in file:
        line = line.rstrip()
        if not line:
            break
        
        start, end = tuple(map(int, line.split('-')))
        fresh_ranges = add_range(start, end, fresh_ranges)

total_fresh = 0
new_ranges = fresh_ranges
while True:
    fresh_ranges = new_ranges
    new_ranges = []
    total_fresh = 0
    for s, e in fresh_ranges:
        new_ranges = add_range(s, e, new_ranges)
        total_fresh += e - s + 1

    if len(new_ranges) == len(fresh_ranges):
        break

print(total_fresh)
