from curses.ascii import isdigit


def apply_map_to_ranges(map, destinations):
    new_destinations = []

    temp_destinations = destinations
    for entry in map:

        un_mapped = []
        while len(temp_destinations) > 0:
            dest = temp_destinations.pop()
            dest_first, dest_last = dest[0], dest[1]
            map_first, map_last = entry[1], entry[1] + entry[2] - 1
            offset = entry[0] - entry[1]
            #Check overlap
            if dest_first <= map_last and dest_last >= map_first:

                #dest in map
                if dest_first >= map_first and dest_last <= map_last:
                    dest[0] += offset
                    dest[1] += offset
                    new_destinations.append(dest)

                #dest start in map
                elif dest_first >= map_first and dest_last > map_last:
                    new_dest = [dest[0], dest[1]]
                    dest[0] = map_last+1
                    un_mapped.append(dest)
                    new_dest[1] = map_last
                    new_dest[0] += offset
                    new_dest[1] += offset
                    new_destinations.append(new_dest)


                #dest_last in map
                elif dest_first < map_first and dest_last <= map_last:
                    new_dest = [dest[0], dest[1]]
                    dest[1] = map_first - 1
                    un_mapped.append(dest)
                    new_dest[0] = map_first
                    new_dest[0] += offset
                    new_dest[1] += offset
                    new_destinations.append(new_dest)

                #map in dest
                elif dest_first < map_first and dest_last > map_last:
                    new_dest1 = [dest[0], map_first - 1]
                    new_dest2 = [map_last+1, dest[1]]
                    new_dest3 = [map_first + offset, map_last + offset]
                    un_mapped.append(new_dest1)
                    un_mapped.append(new_dest2)
                    new_destinations.append(new_dest3)
            else:
                un_mapped.append(dest)
        temp_destinations = un_mapped
    if(len(un_mapped) > 0):
        new_destinations =new_destinations + un_mapped
    return new_destinations



def run(input):
    sections = input.split(":")
    cleaned_sections = []
    for s in sections:
        x = s.splitlines()
        section = []
        for line in x:
            line = line.strip()
            if len(line)>0 and isdigit(line[0]):
                arr = line.split(" ")
                arr2 = [int(i) for i in arr]
                section.append(arr2)
        cleaned_sections.append(section)
    seeds_raw = cleaned_sections[1][0]
    maps = cleaned_sections[2::]

    #order seeds
    seeds = []
    for i in range(0, len(seeds_raw),2):
        start_seed = seeds_raw[i]
        end_seed = start_seed + seeds_raw[i+1] - 1
        seed_interval = [start_seed, end_seed]
        seeds.append( seed_interval)

    # make seed to location mapping
    print("done")
    destinations = seeds
    for map in maps:
        destinations = apply_map_to_ranges(map, destinations)

    destinations.sort()
    print(destinations)



def preprocess(input):
    pass


input = open("in5.txt").read()

#x = preprocess(input)
run(input)