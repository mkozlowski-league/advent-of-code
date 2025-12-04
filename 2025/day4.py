grid = []
total = 0

def count_surrounding(row, col, char):
    """Count the number of a given character in the 8 positions around (row, col)."""
    count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Check all 8 directions
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    for dc, dr in directions:
        r = row + dr
        c = col + dc
        
        # Check if the position is within bounds
        if 0 <= r < rows and 0 <= c < cols:
            if grid[r][c] == char:
                count += 1
    
    return count


with open("day4input.txt", 'r') as file:
    for line in file:
        line = line.rstrip()
        grid.append(list(line))

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char == '@' and count_surrounding(r, c, '@') < 4:
            total += 1
print(total)