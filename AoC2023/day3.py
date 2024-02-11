from curses.ascii import isdigit

val_map = {}

def check_valid_number(start_index, end_index, rownbr, cols, rows, input, number):
    global val_map
    if start_index - 1 >= 0:
        start_index -= 1
        pass

    #check row above
    for i in range(3):
        row = rownbr - 1 + i
        if row >= 0 and row < rows:
            j = start_index
            while j <= end_index:
                val = input[row][j]
                if not isdigit(val) and val != "." and ord(val)!= 10:

                   # print("Found " + str(ord(val)) + " " + str(row) + ":" + str(j))
                    if val == "*":
                        key = str(row) + ":" + str(j)
                        print(val_map.keys())
                        if key in val_map.keys():
                            old = val_map[key]
                            old.append(number)
                            val_map[key] = old
                        else:
                            val_map[key] = [number]

                    return True
                j += 1
    return False


def run(input):
    rows = len(input)
    cols = len(input[0])
    global val_map

    #check if is digit
    #check length and save value and indicies
    #check souroundings

    valid_numbers = []

    for i in range(rows):
        j = 0
        while j < cols-1:
            #if digit
            if isdigit(input[i][j]):
                #get indicies and number
                start_index = j
                while isdigit(input[i][j]) and j < cols-1:
                    j += 1
                end_index = j

                number = int(input[i][start_index:end_index])
                if i == 137:
                    print("a")
                if check_valid_number(start_index, end_index, i, cols, rows, input, number):
                    valid_numbers.append(number)
            else:
                j += 1

    Sum = sum(valid_numbers)
    print(Sum)



def preprocess(input):
    pass

input = open("in3.txt").readlines()

#x = preprocess(input)
run(input)
print(val_map)
sum = 0
for x in val_map.values():
    if len(x) == 2:
        sum += x[0]*x[1]
print(sum)

#550354 - too high