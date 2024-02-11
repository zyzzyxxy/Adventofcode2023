

def run(input):
    conn_north = ['|', 'L', 'J']
    conn_south = ['|', '7', 'F']
    conn_east = ['-', 'L', 'F']
    conn_west = ['-', 'J', '7']

    #find starting pos

    route = []
    coordinates = []
    for line in input:
        if line.__contains__('S'):
            start_row = input.index(line)
            start_col = line.index('S')
    route.append('S')
    #find starting direction
    #right, up, down
    came_from = ''
    row, col = 0,0
    right_pipe = input[start_row][start_col+1]
    down_pipe = input[start_row+1][start_col]
    up_pipe = input[start_row-1][start_col]
    if right_pipe in conn_west:
       # route.append(right_pipe)
        came_from = 'west'
        row, col = start_row, start_col + 1
        current_pipe = right_pipe
    elif down_pipe in conn_north:
        # route.append(down_pipe)
        came_from = 'north'
        row, col = start_row + 1, start_col
        current_pipe = down_pipe
    elif up_pipe in conn_south:
        # route.append(up_pipe)
        came_from = 'south'
        row, col = start_row - 1, start_col
        current_pipe = up_pipe
    else:
        # Handle the case when the starting position does not match any known pipe
        print("Invalid starting position. Please check the map.")

    coordinates.append([start_row, start_col])
    while current_pipe != 'S':
        route.append(current_pipe)
        coordinates.append([row, col])

        if came_from == 'west':
            if current_pipe in conn_north:
                came_from = 'south'
                row, col = row - 1, col
            elif current_pipe in conn_east:
                came_from = 'west'
                row, col = row, col + 1
            elif current_pipe in conn_south:
                came_from = 'north'
                row, col = row + 1, col

        elif came_from == 'east':
            if current_pipe in conn_north:
                came_from = 'south'
                row, col = row - 1, col
            elif current_pipe in conn_west:
                came_from = 'east'
                row, col = row, col - 1
            elif current_pipe in conn_south:
                came_from = 'north'
                row, col = row + 1, col

        elif came_from == 'north':
            if current_pipe in conn_south:
                came_from = 'north'
                row, col = row + 1, col
            elif current_pipe in conn_east:
                came_from = 'west'
                row, col = row, col + 1
            elif current_pipe in conn_west:
                came_from = 'east'
                row, col = row, col - 1

        elif came_from == 'south':
            if current_pipe in conn_north:
                came_from = 'south'
                row, col = row - 1, col
            elif current_pipe in conn_east:
                came_from = 'west'
                row, col = row, col + 1
            elif current_pipe in conn_west:
                came_from = 'east'
                row, col = row, col - 1
        current_pipe = input[row][col]

    print(route)
    print(start_col, start_row)
    print(input[start_row][start_col])
    print(len(route)/2)
    print(coordinates)

    node_map = {}

    for cord in coordinates:
        key = cord[0]
        val = cord[1]
        if key not in node_map.keys():
            node_map[key] = [val]
        else:
            node_map[key].append(val)

    tot_tiles = 0
    rows, cols = len(input), len(input[0])
    for r in range(rows):
        for c in range(cols):
            coord = [r,c]
            walls = 0
            if coord not in coordinates:
                for i in range(c, cols-1):
                    cell = input[r][i]
                    if cell in ['|', 'J', '7']:
                        walls += 1
            if walls%2 == 1:
                tot_tiles += 1



    # for key in node_map.keys():
    #     arr = node_map[key]
    #     arr.sort()
    #     #calc delta
    #     delta = 0
    #     while len(arr) > 1:
    #         val1, val2 = arr.pop(0), arr.pop(0)
    #         delta += val2-val1 - 1
    #     tot_tiles += delta
    #     print(key, delta)




    print(tot_tiles)





input = open("in10test.txt").readlines()

#x = preprocess(input)
run(input)