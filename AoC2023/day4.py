import math
from curses.ascii import isdigit


def run(input):
    totsum = 0
    length = len(input)
    repeat_arr = [1]*length
    games = 0
    for i in range(length):
        print("working on: " + str(i))
        while repeat_arr[i] > 0:
            games += 1
            l = input[i]
            x = l.replace("|", ":").split(":")
            winning, numbers = x[1].strip().replace("  ", " ").split(" "), x[2].strip().replace("  ", " ").split(" ")
            #print(winning, numbers)
            counter = 0
            w_set = set(winning)
            for w in w_set:
                if w in numbers:
                    counter += 1
            while counter > 0:
                repeat_arr[i + counter] += 1
                counter -= 1

            repeat_arr[i] -=1

    print(games)

input = open("in4.txt").readlines()

run(input)


#52862 too high
#40906 too high