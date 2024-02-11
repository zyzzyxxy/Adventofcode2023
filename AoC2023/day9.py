

def run(input):
    lines = []
    for i in input:
        lines.append([int(x) for x in i.split()])

    tot_sum = 0

    for serie in lines:
        diff_lines = []
        current = serie
        while current[-1] != 0:
            diffs = []
            for i in range(1, len(current)):
                diffs.append(current[i] - current[i-1])

            all_zero = any(diffs)
            if(all_zero):
                diff_lines.append(diffs)
            current = diffs
        for i in reversed(range(1, len(diff_lines))):
            val = diff_lines[i][-1] + diff_lines[i-1][-1]
            diff_lines[i-1].append(val)
            #2
            val2 = -diff_lines[i][0] + diff_lines[i-1][0]
            diff_lines[i-1].insert(0, val2)



        new_val = serie[-1]+diff_lines[0][-1]
        new_val2 = serie[0] - diff_lines[0][0]
        serie.append(new_val)
        serie.insert(0, new_val2)
        print(serie)
        tot_sum += serie[0]


    print(tot_sum)



input = open("in9.txt").readlines()

run(input)