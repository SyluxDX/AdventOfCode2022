import argparse
import logging
import copy

def parse_package(package_string, start=1):

    package = []
    buffer = ""
    i = start
    while i < len(package_string):
        char = package_string[i]
        if char == ",":
            if buffer:
                package.append(int(buffer))
                buffer = ""
        elif char == "[":
            nested, i = parse_package(package_string, i+1)
            package.append(nested)
        elif char == "]":
            if buffer:
                package.append(int(buffer))
            return package, i
        else:
            # number
            buffer += char
        # next character
        i += 1

    logging.debug("error: parsing")
    return package, i

def check_order(left_package, right_package, indent=""):
    """ check order results:
    -1 -> not in order (right is lower)
     0 -> can't order, continue
     1 -> in order (left is lower)
    """
    while True:
        # check for empty packages
        if len(left_package) == 0 and len(right_package) == 0:
            return 0
        if len(left_package) == 0:
            logging.debug(f"{indent}  - Left side ran out of items, so inputs are in the right order")
            return 1
        if len(right_package) == 0:
            logging.debug(f"{indent}  - Right side ran out of items, so inputs are not in the right order")
            return -1
        left = left_package.pop(0)
        right = right_package.pop(0)
        logging.debug(f"{indent}- Compare {left} vs {right}")
        # check for Mixed types
        if isinstance(left, list) and isinstance(right, int):
            right = [right]
            logging.debug(f"{indent}  - Mixed types; convert right to {right} and retry comparison")
            # nested comparison:
            result = check_order(left, right, indent+"  ")
            if result:
                return result
        elif isinstance(left, int) and isinstance(right, list):
            left = [left]
            logging.debug(f"{indent}  - Mixed types; convert left to {left} and retry comparison")
            # nested comparison:
            result = check_order(left, right, indent+"  ")
            if result:
                return result
        if isinstance(left, list) and isinstance(right, list):
            result = check_order(left, right, indent+"  ")
            if result:
                return result
        else:
            # compare integers
            if left < right:
                logging.debug(f"{indent}  - Left side is smaller, so inputs are in the right order")
                return 1
            if right < left:
                logging.debug(f"{indent}  - Right side is smaller, so inputs are not in the right order")
                return -1
    return 0

def package_order():
    # read input file
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = ifp.read().rstrip()
    # logging.debug(data)

    ## split pair packages
    package_pairs = data.split("\n\n")
    # process each pair
    sum_index = 0
    for i, pair in enumerate(package_pairs):
        package_pair = [parse_package(package)[0] for package in pair.split("\n")]
        logging.debug(f"== Pair {i+1} ==")
        logging.debug(f"comparing {package_pair[0]} vs {package_pair[1]}")
        result = check_order(package_pair[0], package_pair[1])
        if result == 1:
            sum_index += i+1
        logging.debug("")
    print("Sum of the indices in order:", sum_index)

def get_decoder_key():
    # read input file
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = ifp.read().rstrip().replace("\n\n", "\n")
    logging.debug(data)
    # parse each package
    packages = [parse_package(line)[0] for line in data.split("\n")]
    # add divider packets to list of packages
    packages.append([[2]])
    packages.append([[6]])

    logging.debug("start bubble sort")
    ## bubbleSort
    n = len(packages)
    # Traverse through all array elements
    for i in range(n):
        for j in range(0, n-i-1):
            result = check_order(
                copy.deepcopy(packages[j]),
                copy.deepcopy(packages[j+1]),
            )
            if result == -1:
                packages[j], packages[j+1] = packages[j+1], packages[j]
    logging.debug("end bubble sort")
    # get index of divider packets
    first_divider = packages.index([[2]]) + 1
    second_divider = packages.index([[6]]) + 1
    print("first_divider", first_divider)
    print("second_divider", second_divider)

    print("Decoder key:", first_divider * second_divider)

if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description='Day x Puzzle 1')
    _parser.add_argument('-i', '--input', help='Puzzle input')
    _parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    ARGS = _parser.parse_args()

    if ARGS.verbose:
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        get_decoder_key()
