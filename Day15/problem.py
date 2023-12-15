def problem1():
    """part 1 of the problem."""
    total = 0
    with open('problem.txt') as file:
        input = file.read().strip().split(",")
        multiplier = 17
        divisor = 256
        for term in input:
            val = 0
            for char in term:
                val = ((val + ord(char)) * multiplier) % divisor
            total += val
    return total

def problem2():
    """part 2 of the problem."""
    total = 0
    with open('problem.txt') as file:
        input = file.read().strip().split(",")
        multiplier = 17
        divisor = 256
        hashmap = {i: [] for i in range(0, 256)}
        for term in input:
            if '=' in term:
                # get label and lens
                label, lens = term.split("=")
                # get hash
                val = 0
                for char in label:
                    val += ord(char)
                    val *= multiplier
                    val %= divisor
                # determine if present or not
                row = hashmap[val]
                present = False
                for term in row:
                    if term[0] == label:
                        term[1] = lens
                        present = True
                if not present:
                    row.append([label, lens])
            if '-' in term:
                # get label
                label = term.replace('-', "")
                # get hash
                val = 0
                for char in label:
                    val += ord(char)
                    val *= multiplier
                    val %= divisor
                # determine if present or not
                row = hashmap[val]
                present = False
                index = -1
                for i, term in enumerate(row):
                    if term[0] == label:
                        present = True
                        index = i
                if present:
                    hashmap[val].pop(index)
        # total it up
        for hashh, row in hashmap.items():
            if len(row) > 0:
                for i, pair in enumerate(row):
                    total  += (int(hashh) + 1) * (i + 1) * int(pair[1])
    return total

if __name__ == '__main__':
    print(problem1())
    print(problem2())
