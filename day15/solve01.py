import argparse
import logging
import re

def find_not_beacon():
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = ifp.read().rstrip()

    regex = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")
    beacons = []
    sensores = []
    map_column_min = None
    map_column_max = None
    map_row_min = None
    map_row_max = None
    for line in data.split("\n"):
        positions = regex.search(line)
        if map_column_min is None:
            map_column_min = min(int(positions.groups()[0]), int(positions.groups()[2]))
            map_column_max = max(int(positions.groups()[0]), int(positions.groups()[2]))

            map_row_min = min(int(positions.groups()[1]), int(positions.groups()[3]))
            map_row_max = max(int(positions.groups()[1]), int(positions.groups()[3]))

        sensores.append((
            int(positions.groups()[0]),
            int(positions.groups()[1]),
        ))
        beacons.append((
            int(positions.groups()[2]),
            int(positions.groups()[3]),
        ))
        map_column_min = min(map_column_min, int(positions.groups()[0]), int(positions.groups()[2]))
        map_column_max = max(map_column_max, int(positions.groups()[0]), int(positions.groups()[2]))
        map_row_min = min(map_row_min, int(positions.groups()[1]), int(positions.groups()[3]))
        map_row_max = max(map_row_max, int(positions.groups()[1]), int(positions.groups()[3]))

    print("map_column_min", map_column_min)
    print("map_column_max", map_column_max)
    print("map_row_min", map_row_min)
    print("map_row_max", map_row_max)

    for i in range(len(beacons)):
        print(sensores[i], beacons[i])
    ## for each pair on beacon sensor calculate Manhattan distance
    # then for each cell in row check if cell is closer to sensor

if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description="Day 14 Puzzle 2")
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
        find_not_beacon()
