def problem1():
    """part 1 of the problem."""
    with open('problem.txt') as file:
        seeds = [int(i) for i in file.readline().split(":")[1].split()]
        file.readline()
        sections = file.read().split("\n\n")
        for section in sections:
            maps = [[int (i) for i in x.split()] for x in section.split('\n')[1:]]
            shifts = [{"destination": mp[0], "start": mp[1], "end": mp[1] + mp[2] - 1} for mp in maps]
            for i, seed in enumerate(seeds):
                for shift in shifts:
                    if seed >= shift["start"] and seed <= shift["end"]:
                        seeds[i] = seeds[i] - shift["start"] + shift["destination"]
                        break
    return min(seeds)


def problem2():
    """part 2 of the problem."""
    with open('example.txt') as file:
        seed_pairs = [int(i) for i in file.readline().split(":")[1].split()]
        seed_ranges = []
        for i in range(0, len(seed_pairs), 2):
            seed_ranges.append({"start": seed_pairs[i], "end": seed_pairs[i] + seed_pairs[i + 1] - 1})
        file.readline()
        sections = file.read().split("\n\n")
        for section in sections:
            maps = [[int (i) for i in x.split()] for x in section.split('\n')[1:]]
            shifts = [{"destination": mp[0], "start": mp[1], "end": mp[1] + mp[2] - 1} for mp in maps]
            print(seed_ranges, '\n', shifts)
    #         for i, seed in enumerate(seeds):
    #             for shift in shifts:
    #                 if seed >= shift["start"] and seed <= shift["end"]:
    #                     seeds[i] = seeds[i] - shift["start"] + shift["destination"]
    #                     break
    #                 print(shift)
    # return min(seeds)

if __name__ == '__main__':
    # print(problem1())
    print(problem2())
