total = 0

# Read and process the input line
with open("day2input.txt", 'r') as file:
    line = file.readline()

pairs = line.rstrip().split(',')
for pair in pairs:
    pair = pair.split('-')
    start, end = int(pair[0]), int(pair[1])

    for num in range(start, end + 1):
        id = str(num)

        pattern = id[0]
        longest_pattern = pattern
        in_pattern = False
        i = 1
        while i < len(id):
            if id[i : i+len(pattern)] == pattern:
                longest_pattern += id[i : i+len(pattern)]
                in_pattern = True
                i += len(pattern)
            else:
                if in_pattern:
                    pattern = longest_pattern
                    in_pattern = False
                pattern += id[i]
                longest_pattern = pattern
                i += 1
        
        if in_pattern:
            total += num

print(total)