tiles = []
with open("testin.txt", 'r') as file:
    for line in file:
        line = line.rstrip()
        tiles.append(tuple(map(int, line.split(','))))

def area(tile1, tile2):
    return (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)

max_area = 0
max_area_tiles = []
for i, tile1 in enumerate(tiles):
    for j, tile2 in enumerate(tiles):
        if i == j:
            continue
        a = area(tile1, tile2)
        if a > max_area:
            max_area = a
            max_area_tiles = [tile1, tile2]
print(max_area)
print(max_area_tiles)