import argparse

def check_marker(msg):
    if len(msg) != 4:
        return False
    return len(set(msg)) == 4

def find_marker():
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = ifp.read().rstrip().split()

    for msg in data:
        buffer = []
        i = 0
        for char in msg:
            i += 1
            buffer.append(char)
            if len(buffer) == 5:
                buffer.pop(0)
            if check_marker(buffer):
                print("marker at:", i)
                break
    

if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description="Day 6 Puzzle 1")
    _parser.add_argument("-i", "--input", help="Puzzle input")
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        find_marker()
