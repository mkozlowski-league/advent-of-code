
import pulp #🤮

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
        max_joltage = max(joltage)

        prob = pulp.LpProblem("Day10P2", pulp.LpMinimize)
        
        vars = [pulp.LpVariable(f"x{i}", 0, max_joltage + 1, cat='Integer') for i in range(len(buttons))]

        for i in range(len(joltage)):
            button_vars = [vars[b] for b, button in enumerate(buttons) if i in button]
            prob += pulp.lpSum(button_vars) == joltage[i]
        prob += pulp.lpSum(vars)

        prob.solve(pulp.PULP_CBC_CMD(msg=False))

        # for v in vars:
        #     print(v, "=", pulp.value(v))
        
        print(pulp.value(prob.objective))
        total += pulp.value(prob.objective)

print(int(total))