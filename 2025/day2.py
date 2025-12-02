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
        mid = len(id) // 2
        if len(id) % 2 == 0 and id[:mid] == id[mid:]:
            total += num

print(total)