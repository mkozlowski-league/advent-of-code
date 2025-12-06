import math

# Read in as a 2D array of characters
grid = []
with open("day6input.txt", 'r') as file:
    for line in file:
        grid.append(list(line))

grand_total = 0
numbers = []
for c in range(len(grid[0]) - 1, -1, -1):
    num_str = ""
    for row in grid:
        # Ignore spaces and the newlines
        if '0' <= row[c] <= '9':
            num_str += row[c]
        elif row[c] == '+' or row[c] == '*':
            numbers.append(int(num_str))
            grand_total += sum(numbers) if row[c] == '+' else math.prod(numbers) # You're killing me python
            num_str = ""
            numbers = []

    if num_str:
        numbers.append(int(num_str))

print(grand_total)