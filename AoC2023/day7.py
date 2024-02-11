from curses.ascii import isdigit
card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}


def level_sort(level):
    global card_values
    result = []
    for hand in level:
        counter = 0
        for val in result:
            hand_larger = False
            #check largest
            for i in range(5):
                hand_value = card_values[hand[i]]
                val_value = card_values[val[i]]
                if hand_value > val_value:
                    hand_larger = True
                    break
                elif hand_value < val_value:
                    break
            if hand_larger is True:
                break
            else:
                counter += 1
        result.insert(counter, hand)

    return result



def card_sort(input):
    global card_values
    hands = [[],[],[],[],[],[],[]]
    for line in input:
        hand = line.split()[0]
        card_map = {}
        joker_count = 0
        for c in hand:
            if c == 'J':
                joker_count += 1
            else:
                if c in card_map.keys():
                    card_map[c] += 1
                else:
                    card_map[c] = 1


        values = sorted(list(card_map.values()), reverse=True)
        if joker_count == 5:
            hands[0].append(line)
        # Five of a kind
        elif(values[0] + joker_count == 5):
            hands[0].append(line)
        # Four of a kind
        elif (values[0] + joker_count == 4):
            hands[1].append(line)
        # Full house
        elif (values[0] + joker_count == 3 and values[1] == 2):
            hands[2].append(line)
        # Three of a kind
        elif (values[0] + joker_count == 3 and values[1] == 1):
            hands[3].append(line)
        # Two pair
        elif (values[0] + joker_count == 2 and values[1] == 2):
            hands[4].append(line)
        # One pair
        elif (values[0] + joker_count == 2 and values[1] == 1):
            hands[5].append(line)
        # High card
        elif(values[0] + joker_count == 1):
            hands[6].append(line)

    sorted_hands = []
    for i in range(len(hands)):
        level = hands[i]
        sorted_level = level_sort(level)
        sorted_hands.extend(sorted_level)

    #Calc values
    rank = len(sorted_hands)
    totsum = 0
    for i in range(len(sorted_hands)):
        hand_val = int(sorted_hands[i].split()[1])
        totsum += hand_val*rank
        rank -= 1
    print(totsum)



def run(input):
    sorted = card_sort(input)

input = open("in7.txt").readlines()

#x = preprocess(input)
run(input)