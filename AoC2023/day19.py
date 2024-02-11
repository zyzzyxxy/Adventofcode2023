from curses.ascii import isdigit


def run(input):
    sum = 0
    for l in input:
        numbers = list(filter(lambda c: (isdigit(c)), l))
    print(sum)



def preprocess(input):
    pass


input = open("in2.txt").readlines()

#x = preprocess(input)
run(input)