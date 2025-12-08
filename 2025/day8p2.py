boxes = []
with open("day8input.txt", 'r') as file:
    for line in file:
        line = line.rstrip()
        boxes.append(tuple(map(int, line.split(','))))

# Square roots aren't real
def distance(box1, box2):
    return (box1[0] - box2[0])**2 + (box1[1] - box2[1])**2 + (box1[2] - box2[2])**2

circuits = []
num_cons = 0
while num_cons < 1000:
    min_dist = float('inf')
    min_connection = None
    for i, box1 in enumerate(boxes):
        for j, box2 in enumerate(boxes):
            if i == j:
                continue
            dist = distance(box1, box2)
            # I don't care what the elves say, don't waste time adding unnecessary connections
            if dist < min_dist and not any(True for c in circuits if {i, j}.issubset(c)):
                min_dist = dist
                min_connection = {i, j}

    overlap_circuits = [c for c in circuits if min_connection & c]
    if len(overlap_circuits) == 0:
        circuits.append(set(min_connection))
        print(f">> New circuit {min_connection}")
    elif len(overlap_circuits) == 1:
        print(f">> Added {min_connection} to {overlap_circuits[0]}")
        overlap_circuits[0].update(min_connection)
    else:
        print(f">> Merged {overlap_circuits[0]} and {overlap_circuits[1]} due to {min_connection}")
        overlap_circuits[0].update(min_connection)
        overlap_circuits[0].update(overlap_circuits[1])
        circuits.remove(overlap_circuits[1])
    
    if num_cons > 10 and len(circuits) == 1 and len(circuits[0]) == 1000:
        [i, j] = list(min_connection)
        print(boxes[i][0] * boxes[j][0])
        break

    num_cons += 1