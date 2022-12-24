import argparse

def check_marker(msg, length):
    if len(msg) != length:
        return False
    return len(set(msg)) == length

def find_marker():
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = ifp.read().rstrip().split()

    for msg in data:
        buffer = []
        i = 0
        for char in msg:
            i += 1
            buffer.append(char)
            if len(buffer) == 15:
                buffer.pop(0)
            if check_marker(buffer, 14):
                print("marker at:", i)
                break
    

if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description="Day 6 Puzzle 2")
    _parser.add_argument("-i", "--input", help="Puzzle input")
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        find_marker()
