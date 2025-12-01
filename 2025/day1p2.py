cur_pos = 50
num_at_0 = 0

# Read and process the input file line by line
with open("day1input.txt", 'r') as file:
    for line in file:
        line = line.rstrip()

        num = int(line[1:])

        if line[0] == 'L':
            next_pos = cur_pos - num
        elif line[0] == 'R':
            next_pos = cur_pos + num
        else:
            raise ValueError(f"Invalid direction: {line[0]}")
        
        if next_pos <= 0:
            #                                +1 if we started off positive
            num_at_0 += int(-next_pos / 100) + int(cur_pos != 0)
        elif next_pos > 99:
            num_at_0 += int(next_pos / 100)

        # Keep cur_pos between 0-99
        cur_pos = next_pos % 100
        
    print(num_at_0)
