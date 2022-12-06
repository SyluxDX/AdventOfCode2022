import argparse

def calories_count():
    """ Count elves calories """
    print(f"Using list in file: {ARGS.input}")
    with open(ARGS.input, "r") as ifp:
        data = ifp.read()
    data_by_elves = data.split("\n\n")

    max_cals = 0
    for cals in data_by_elves:
        sum = 0
        for cal in cals.split("\n"):
            if cal:
                sum += int(cal)
        max_cals = max(max_cals, sum)
    print(f"Elf carrying the most Calories have: {max_cals}")


if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description='Day 1 Puzzle 1')
    _parser.add_argument('-i', '--input', help='Puzzle input')
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        calories_count()
