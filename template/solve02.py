import argparse

def func():
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = ifp.read().rstrip()


if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description="Day x Puzzle 2")
    _parser.add_argument("-i", "--input", help="Puzzle input")
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        func()
