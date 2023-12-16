import numpy as np

with open("day_5/input.txt", "r") as file:
    input = file.read()
    sections = input.split("\n")
    seeds = sections[0].split(" ")
    seeds = seeds[1:]

    # make list with dummy_values of equal length to seeds, called seed_locations
    seed_locations = []
    for i in range(len(seeds)):
        seed_locations.append(int(seeds[i]))

    maps = input.split("\n\n")
    maps = maps[1:]
    for map in maps:
        corresponding_seeds_and_soils = np.arange(10000000000)
        lines = map.split("\n")
        for line in lines[1:]:
            numbers = line.split(" ")
            destination_start = int(numbers[0])
            source_start = int(numbers[1])
            range_length = int(numbers[2])
            corresponding_seeds_and_soils[source_start:source_start+range_length] = np.arange(destination_start, destination_start+range_length, 1)

        print("Mapped out the instrucitons")

        # for all values smaller than the largest item, add in the dictionary as item = key 
        # and item = value
        # for i in range(max(seed_locations)+1):
        #     if i not in corresponding_seeds_and_soils:
        #         corresponding_seeds_and_soils[i] = i
        print("Filled in the blanks")

        # for i in range(100):
        #     if i not in corresponding_seeds_and_soils:
        #         corresponding_seeds_and_soils[i] = i


        for i in range(len(seeds)):
            seed_locations[i] = corresponding_seeds_and_soils[int(seed_locations[i])]
        
        print("Updated the seed locations")

print(min(seed_locations))