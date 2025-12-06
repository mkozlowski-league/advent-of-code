# This will be a grid of the problems, with each column needing to be calculated
problems = [None] # Save space for the operations which we'll put in the first row
with open("day6input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split(' ')

        if parts[0].isdigit():
            problems.append([int(p) for p in parts if p])
        else:
            # Place the row of operations into the first row
            problems[0] = [p for p in parts if p]

grand_total = 0
for c in range(len(problems[0])):
    for row in problems:
        if row[c] == '+':
            operation = row[c]
            accumulator = 0
        elif row[c] == '*':
            operation = row[c]
            accumulator = 1
        elif operation == '+':
            accumulator += row[c]
        elif operation == '*':
            accumulator *= row[c]

    grand_total += accumulator
    operation = ''
    accumulator = None

print(grand_total)