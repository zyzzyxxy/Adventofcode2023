import math


def run(input):
    instructions = list(input[0].strip())
    size = len(input)
    node_map = {}
    for i in range(2, size):
        node, left, right = input[i].replace("="," ").replace("("," ").replace(")"," ").replace(","," ").split()
        node_map[node] = [left, right]


    starting_nodes = [key for key in node_map.keys() if key.endswith("A")]
    last_nodes = [key for key in node_map.keys() if key.endswith("Z")]

    cycles = {}

    for node in starting_nodes:
        cycles[node] = []
        running = True
        steps = 0
        instr = [] +instructions
        temp_node = node
        while running:
            steps += 1
            if instr[0] == 'L':
                temp_node = node_map[temp_node][0]
            else:
                temp_node = node_map[temp_node][1]
            instr.append(instr.pop(0))
            if temp_node in last_nodes:
                tuple = (temp_node, steps)
                if tuple not in cycles[node]:
                    cycles[node].append(tuple)
                    steps = 0
                else:
                    running = False
    print(cycles)



    def gcd(x, y):
        """Return the greatest common divisor of two integers."""
        while y:
            x, y = y, x % y
        return abs(x)

    def lcm(x, y):
        """Return the least common multiple of two integers."""
        return abs(x * y) // gcd(x, y)

    # Example: Find the LCM of 12 and 18
    num1 = 12
    num2 = 18

    result = lcm(num1, num2)
    temp_val = list(cycles.values())[1][0][1]
    for val in list(cycles.values())[1::]:
        temp_val = lcm(temp_val, val[0][1])


    print(f"The LCM of {num1} and {num2} is {result}")



    # steps = 0
    # #running = True
    # while running:
    #     steps += 1
    #     instruction = instructions.pop(0)
    #     instructions.append(instruction)
    #     temp_nodes = []
    #     z_counter = 0
    #     for node in starting_nodes:
    #         if instruction == 'L':
    #             new_node = node_map[node][0]
    #         else:
    #             new_node = node_map[node][1]
    #         temp_nodes.append(new_node)
    #         if new_node[2] == 'Z':
    #             z_counter+=1
    #     starting_nodes = temp_nodes
    #     if z_counter == len(starting_nodes):
    #         running = False
    #
    #     if steps %1000000 == 0:
    #         print("100k")
    #
    # print(steps)

input = open("in8.txt").readlines()

#x = preprocess(input)
run(input)

#225247674731 too low
#13740108158591
#8232733109413031 too high