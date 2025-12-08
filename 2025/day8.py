boxes = []
with open("day8input.txt", 'r') as file:
    for line in file:
        line = line.rstrip()
        boxes.append(tuple(map(int, line.split(','))))

# Square roots aren't real
def distance(box1, box2):
    return (box1[0] - box2[0])**2 + (box1[1] - box2[1])**2 + (box1[2] - box2[2])**2

direct_connections = []
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
            if dist < min_dist and {i, j} not in direct_connections:
                min_dist = dist
                min_connection = {i, j}

    overlap_circuits = [c for c in circuits if min_connection & c]
    if len(overlap_circuits) == 0:
        circuits.append(set(min_connection))
        print(f">> New circuit {min_connection}")
    elif len(overlap_circuits) == 1 and not min_connection.issubset(overlap_circuits[0]):
        # If the connection IS a subset, "nothing happens" except that it still apparently counts as a "connection"
        # This is why the elves are running out of extension cables...they're needlessly adding connections to existing circuits
        print(f">> Added {min_connection} to {overlap_circuits[0]}")
        overlap_circuits[0].update(min_connection)
    elif len(overlap_circuits) == 2:
        print(f">> Merged {overlap_circuits[0]} and {overlap_circuits[1]} due to {min_connection}")
        overlap_circuits[0].update(min_connection)
        overlap_circuits[0].update(overlap_circuits[1])
        circuits.remove(overlap_circuits[1])

    direct_connections.append(min_connection)
    num_cons += 1

lengths = sorted([len(c) for c in circuits])
print(circuits)
print(lengths[-1] * lengths[-2] * lengths[-3])
