from curses.ascii import isdigit


def run(input):
    sum = 0
    for l in input:
        numbers = list(filter(lambda c: (isdigit(c)), l))
        n = numbers[0]+numbers[-1]
        num = int(n)
        sum += num
    print(sum)



def preprocess(input):
    result = []

    digit_mapping = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    for l in input:
        print(l)
        new_line = ""
        l_len = len(l)
        for i in range(l_len):
            if isdigit(l[i]):
                new_line += l[i]
            else:
                for spelled, digit in digit_mapping.items():
                    size = len(spelled)
                    if i + size <= l_len:
                        if l[i:i+size] == spelled:
                            new_line += digit
        print(new_line)
        result.append(new_line)
    return result






input = open("in1.txt").readlines()

x = preprocess(input)
run(x)