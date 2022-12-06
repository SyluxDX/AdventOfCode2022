import argparse

def top_three_calories():
    """ Count elves calories """
    print(f"Using list in file: {ARGS.input}")
    with open(ARGS.input, "r") as ifp:
        data = ifp.read()
    data_by_elves = data.split("\n\n")

    max_cals = list()
    for cals in data_by_elves:
        sum = 0
        for cal in cals.split("\n"):
            if cal:
                sum += int(cal)
        max_cals.append(sum)
    # sort desc max_cals list
    max_cals.sort(reverse=True)
    total = 0
    for cal in max_cals[:3]:
        total += cal
    print(f"Top threes Elfs that are carrying the most Calories have: {total}")


if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description='Day 1 Puzzle 2')
    _parser.add_argument('-i', '--input', help='Puzzle input')
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        top_three_calories()
