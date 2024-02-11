import math
from curses.ascii import isdigit


def pq_formula(time, distance):
    #x*time-x=distance
    #-x^2 + time*x - distance = 0
    #x^2 - times*x + distance = 0
    p = -time
    q = distance
    x1 = -p / 2 - math.sqrt(pow(p / 2, 2) - q) + 0.0001
    x2 = -p / 2 + math.sqrt(pow(p / 2, 2) - q) - 0.0001
    #print(x1)

    return x1, x2

def run(input):
    times = "".join(input[0].split(":")[1].strip().split())
    #times = [int(i) for i  in times]
    distances = "".join(input[1].split(":")[1].strip().split())
    #distances = [int(i) for i in distances]

    run_times = len(times)

    res = 1
    for i in range(1):
        x1, x2 = pq_formula(int(times), int(distances))
        shortest = math.ceil(x1)
        longest = math.floor(x2)
        ways_to_win = longest-shortest + 1
        res =res*ways_to_win
        print(ways_to_win)
    print(res)


def preprocess(input):
    pass


input = open("in6.txt").readlines()

#x = preprocess(input)
run(input)