def main():
    filepath = "./day3/input1.txt"
    fp = open(filepath)
    wire_path1 = fp.readline()
    wire_path2 = fp.readline()

    wire_path1 = wire_path1.split(',')
    wire_path2 = wire_path2.split(',')

    points1 = solve(wire_path1)
    points2 = solve(wire_path2)

    intersection_points = [point for point in points1 if point in points2]
    print(intersection_points)

    closest = min(points1[point] + points2[point] for point in intersection_points)
    print(closest)

    fp.close()

def solve(path):
    curr_x = curr_y = step = 0
    directions = {'R':(1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1)}
    points = {}
    for move in path:
        dx, dy = directions[move[0]]
        for _ in range(int(move[1:])):
            curr_x += dx
            curr_y += dy
            step += 1
            if (curr_x, curr_y) not in points:
                points[(curr_x, curr_y)] = step
        
    return points



if __name__ == "__main__":
    main()