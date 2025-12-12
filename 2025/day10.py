def toggle_bits(state, bits):
    for b in bits:
        state ^= (1 << b)
    return state

# Generate combinations of button presses (non-decreasing order)
def generate_combinations(length, start_idx=0):
    if length == 0:
        return [[]]
    if length == 1:
        return [[i] for i in range(start_idx, len(buttons))]
    
    result = []
    for i in range(start_idx, len(buttons)):
        for combo in generate_combinations(length - 1, i):
            result.append([i] + combo)
    return result

total = 0
with open("day10input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        
        end_bracket = line.find(']')
        lights = line[end_bracket - 1 : 0 : -1]
        lights = lights.replace('.', '0').replace('#', '1')
        target = int(lights, 2)

        start_brace = line.find('{')

        button_strs = line[end_bracket + 2:start_brace - 1].split(' ')
        buttons = [list(map(int, b[1:-1].split(','))) for b in button_strs]
        
        joltage = list(map(int, line[start_brace + 1:-1].split(',')))
        
        # Test all combinations up to 10
        for press_count in range(1, 11):
            combinations = generate_combinations(press_count)
            for combo in combinations:
                state = 0
                for button_idx in combo:
                    state = toggle_bits(state, buttons[button_idx])
                
                if state == target:
                    total += len(combo)
                    break
            else:
                continue
            break
        else:
            print(f"No solution <10 for target {target}")
            exit(1)

print(total)
