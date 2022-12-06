import argparse
import string

priority = list(string.ascii_lowercase + string.ascii_uppercase)

def rucksack_priority():
    with open(ARGS.input, "r", encoding="utf8") as ifp:
        input_data = ifp.read().strip()
    rucksacks = input_data.split("\n")

    i = 0
    total = 0
    while i < len(rucksacks):
        bag1 = list(rucksacks[i])
        bag2 = list(rucksacks[i+1])
        bag3 = list(rucksacks[i+2])

        # compare bag1 with bag2 and get possible badges
        possible_badges = list()
        for item in bag2:
            if item in bag1:
                possible_badges.append(item)
        # find badge by comparing possible badges with bag3
        for item in bag3:
            if item in possible_badges:
                total += priority.index(item)+1
                break
        i += 3
    print(f"Total: {total}")



if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description='Day x Puzzle 1')
    _parser.add_argument('-i', '--input', help='Puzzle input')
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        rucksack_priority()
