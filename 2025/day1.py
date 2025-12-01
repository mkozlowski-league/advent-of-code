cur_pos = 50
num_at_0 = 0

# Read and process the input file line by line
with open("day1input.txt", 'r') as file:
    for line in file:
        line = line.rstrip()

        # String based mod 100
        rem_str = line[-2:] if len(line) > 2 else line[1:]
        num = int(rem_str)

        # Convert to addition
        if line[0] == 'L':
            num = 100 - num
        elif line[0] != 'R':
            raise ValueError(f"Invalid direction: {line[0]}")
        
        cur_pos += num
        if cur_pos > 99:
            cur_pos -= 100
        
        if cur_pos == 0:
            num_at_0 += 1
        
    print(num_at_0)
