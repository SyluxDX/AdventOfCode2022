import argparse
import string

priority = list(string.ascii_lowercase + string.ascii_uppercase)

def rucksack_priority():
    with open(ARGS.input, "r", encoding="utf8") as ifp:
        input_data = ifp.read().strip()
    rucksacks = input_data.split("\n")

    total = 0
    for bag in rucksacks:
        compart1 = list(bag[:len(bag)//2])
        compart2 = list(bag[len(bag)//2:])

        for item in compart2:
            if item in compart1:
                total += priority.index(item)+1
                break
    print(f"Total: {total}")

if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description='Day x Puzzle 1')
    _parser.add_argument('-i', '--input', help='Puzzle input')
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        rucksack_priority()
