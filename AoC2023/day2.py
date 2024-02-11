from functools import reduce


def run(input):
    color_map = {
        "red" : 12,
        "green" : 13,
        "blue"  : 14
    }
    sum = 0

    for l in input:
        x = l.split(": ")
        id = int(x[0][5:])
        valid = True
        subsets = x[1].split(";")

        color_map_2 = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for set in subsets:
            if not valid:
                #print("Breaking")
                break;
            cubes = set.split(",")



            for cube in cubes:
                c = cube.strip().split(" ")
                amount = int(c[0])
                color = c[1]
                limit = color_map_2.get(color)
                if amount > limit:
                    color_map_2[color] = amount

        x = color_map_2.values()
        y = reduce((lambda x, y: x * y), x)
        print(y)
        sum+=y

    print(sum)






def preprocess(input):
    pass


input = open("in2.txt").readlines()

#x = preprocess(input)
run(input)