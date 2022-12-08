import argparse

def overlap_count():
    with open(ARGS.input, "r", encoding="utf8") as ifp:
        data = [x.replace("-",",").split(",") for x in ifp.read().strip().split("\n")]
        assignments = []
        for x in data:
            assignments.append([(int(x[0]),int(x[1])), (int(x[2]),int(x[3]))])

    overlaps = 0
    for elm in assignments:
        first = elm[0]
        seconds = elm[1]
        if first[0]>=seconds[0] and first[1]<=seconds[1]:
            overlaps += 1
        elif seconds[0]>=first[0] and seconds[1]<=first[1]:
            overlaps += 1
        else:
            pass
    print("Overlaps:", overlaps)

if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description='Day x Puzzle 1')
    _parser.add_argument('-i', '--input', help='Puzzle input')
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        overlap_count()
