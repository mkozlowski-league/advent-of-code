NUM_DIGITS_IN_JOLTAGE = 2

total_joltage = 0

# Read and process the input file line by line
with open("day3input.txt", 'r') as file:
    for line in file:
        line = line.rstrip()

        digits = ["0"] * NUM_DIGITS_IN_JOLTAGE

        max_digit_index = 0
        i = 1
        for n in range(NUM_DIGITS_IN_JOLTAGE):
            # Don't check the last (NUM_DIGITS_IN_JOLTAGE - 1) characters, we need enough for the remaining digits
            while i < len(line) - (NUM_DIGITS_IN_JOLTAGE - 1 - n):
                if line[i] > line[max_digit_index]:
                    max_digit_index = i
                if line[max_digit_index] == "9":
                    break
                i += 1
        
            # Save the digit and continue looking for the next
            digits[n] = line[max_digit_index]
            max_digit_index += 1
            i = max_digit_index + 1

        num = int("".join(digits))
        total_joltage += num

print(total_joltage)