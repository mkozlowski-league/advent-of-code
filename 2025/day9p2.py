def segment_intersects(tile1, tile2, polygon):
    sq_left, sq_right = min(tile1[0], tile2[0]), max(tile1[0], tile2[0])
    sq_top, sq_bottom = min(tile1[1], tile2[1]), max(tile1[1], tile2[1])

    for i in range(len(polygon)):
        xi, yi = polygon[i]
        xj, yj = polygon[(i + 1) % len(polygon)]
        x_min, x_max = min(xi, xj), max(xi, xj)
        y_min, y_max = min(yi, yj), max(yi, yj)

        # Horizontal lines that are vertically within the square, cross the left or right side
        if (y_min == y_max and sq_top < y_max < sq_bottom and
            (x_min <= sq_left < x_max or x_min < sq_right <= x_max)
        ):
            return True
        
        # Vertical lines that are horizontally within the square, cross the top or bottom side
        if (x_min == x_max and sq_left < x_min < sq_right and
            (y_min <= sq_top < y_max or y_min < sq_bottom <= y_max)
        ):
            return True
        
    return False

def area(tile1, tile2):
    return (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)

tiles = []
with open("day9input.txt", 'r') as file:
    for line in file:
        line = line.rstrip()
        tiles.append(tuple(map(int, line.split(','))))

max_area = 0
max_area_tiles = []
for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        if not segment_intersects(tiles[i], tiles[j], tiles):
            a = area(tiles[i], tiles[j])
            if a > max_area:
                max_area = a
                max_area_tiles = [tiles[i], tiles[j]]
                
print(max_area)
print(max_area_tiles)
