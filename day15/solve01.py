import argparse
import logging
import re

def manhattan_distance(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

def find_not_beacon():
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = ifp.read().rstrip()

    regex = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")
    beacons = []
    sensors = []
    for line in data.split("\n"):
        positions = regex.search(line)
        sensors.append((
            int(positions.groups()[0]),
            int(positions.groups()[1]),
        ))
        beacons.append((
            int(positions.groups()[2]),
            int(positions.groups()[3]),
        ))

    # target_row = 2000000
    target_row = 10
    not_beacons = set()
    for i in range(len(beacons)):
        print(f"checking pair {i+1}/{len(beacons)}")
        logging.debug(f"{sensors[i]} {beacons[i]} -> {manhattan_distance(sensors[i], beacons[i])}")

        closest_beacon = manhattan_distance(sensors[i], beacons[i])
        # check distance to target_row
        closest_target_row = (sensors[i][0], target_row)
        if manhattan_distance(sensors[i], closest_target_row) <= closest_beacon:
            # check left
            n = 0
            while True:
                test = (closest_target_row[0]-n, closest_target_row[1])
                if test not in not_beacons:
                    if test not in sensors and test not in beacons:
                        if manhattan_distance(sensors[i], test) <= closest_beacon:
                            not_beacons.add(test)
                        else:
                            break
                n += 1
            # check left
            n = 0
            while True:
                test = (closest_target_row[0]+n, closest_target_row[1])
                if test not in not_beacons:
                    if test not in sensors and test not in beacons:
                        if manhattan_distance(sensors[i], test) <= closest_beacon:
                            not_beacons.add(test)
                        else:
                            break
                n += 1

    print(f"Row {target_row} there are {len(not_beacons)} position(s) where beacon cannot be")

if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description="Day 15 Puzzle 2")
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
