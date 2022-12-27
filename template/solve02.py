import argparse
import logging

def func():
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = ifp.read().rstrip()


if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description="Day x Puzzle 2")
    _parser.add_argument("-i", "--input", help="Puzzle input")
    _parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    _parser.add_argument("-vv", "--very-verbose", help="futher increase output verbosity", action="store_true")
    ARGS = _parser.parse_args()

    if ARGS.verbose:
        logging.basicConfig(level=logging.INFO, format="%(message)s")
    if ARGS.very_verbose:
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        func()
