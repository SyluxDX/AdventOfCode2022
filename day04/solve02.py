import argparse

def overlap_count():
    with open(ARGS.input, "r", encoding="utf8") as ifp:
        data = [x.replace("-",",").split(",") for x in ifp.read().strip().split("\n")]
        assignments = []
        for x in data:
            assignments.append([(int(x[0]),int(x[1])), (int(x[2]),int(x[3]))])

    overlaps = 0
    for elm in assignments:
        first = list(range(elm[0][0], elm[0][1]+1))
        second = list(range(elm[1][0], elm[1][1]+1))
        for x in second:
            if x in first:
                overlaps +=1
                break
    print("Overlaps:", overlaps)

if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description='Day x Puzzle 1')
    _parser.add_argument('-i', '--input', help='Puzzle input')
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        overlap_count()
