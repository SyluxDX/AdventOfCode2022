import argparse
import logging
import re

def manhattan_distance(x, y) -> int:
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

def sensor_beacon_perimeter(sensor, beacon, max_coordinate, min_coordinate=0):
    """ generate perimeter positions clockwise, starting at left or 9 o'clock """

    perimeter = []
    distance = manhattan_distance(sensor, beacon) + 1
    for i in range(distance):
        # right up
        aux = (sensor[0]+i-distance, sensor[1]-i)
        if (aux[0] >= min_coordinate and aux[0] <= max_coordinate and
            aux[1] >= min_coordinate and aux[1] <= max_coordinate):
            perimeter.append(aux)
        # right down
        aux = (sensor[0]+i, sensor[1]+i-distance)
        if (aux[0] >= min_coordinate and aux[0] <= max_coordinate and
            aux[1] >= min_coordinate and aux[1] <= max_coordinate):
            perimeter.append(aux)
        # left down
        aux = (sensor[0]-i+distance, sensor[1]+i)
        if (aux[0] >= min_coordinate and aux[0] <= max_coordinate and
            aux[1] >= min_coordinate and aux[1] <= max_coordinate):
            perimeter.append(aux)
        # left up
        aux = (sensor[0]-i, sensor[1]-i+distance)
        if (aux[0] >= min_coordinate and aux[0] <= max_coordinate and
            aux[1] >= min_coordinate and aux[1] <= max_coordinate):
            perimeter.append(aux)

    return perimeter

def find_beacon():
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

    max_coordinate = 4000000
    search_spots = set()
    num_beacon_sensors = len(beacons)
    beacon_found = False

    for i in range(num_beacon_sensors):
        logging.info(f"checking perimeter {i+1}/{num_beacon_sensors}")
        logging.debug(f"generating perimeter for b{beacons[i]} s{sensors[i]}")
        # Generate outside search perimeter
        perimeter = sensor_beacon_perimeter(sensors[i], beacons[i], max_coordinate)
        logging.debug(f"search {len(perimeter)} positions")
        for search in perimeter:
            ## search perimiter position if not already
            if search not in search_spots:
                search_spots.add(search)
                # check if inside beacon range
                outsite = True
                for j in range(num_beacon_sensors):
                    beacon_sensor_dist = manhattan_distance(beacons[j], sensors[j])
                    spot_sensor_dist = manhattan_distance(search, sensors[j])
                    if spot_sensor_dist <= beacon_sensor_dist:
                        outsite = False
                        break

                if outsite:
                    beacon_found = True
                    break
        if beacon_found:
            print(f"Tunning frequency: {search[0]*4000000 + search[1]} (x={search}, y={search[1]})")
            break


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
        find_beacon()
