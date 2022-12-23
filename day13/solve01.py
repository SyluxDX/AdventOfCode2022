import argparse

def parse_package_old(package_string):
    print("parse:", package_string)
    package = []
    buffer = ""
    for i, char in enumerate(package_string):
        print("char", char, i, "buffer:", buffer)
        if char == ",":
            package.append(int(buffer))
            buffer = ""
        elif char == "[":
            package.append(parse_package(package_string[i+1:]))
        elif char == "]":
            package.append(int(buffer))
            print(f"returning", package)
            return package
        else:
            # number
            buffer += char
    
    print("error: parsing")
    return package

def parse_package(package_string, start=1):
    
    package = []
    buffer = ""
    i = start
    while i < len(package_string):
        char = package_string[i]
        # print("parse:", package_string)
        # print("      ", " "*i+"^")
        # print("char", char, i, "buffer:", buffer)
        
        if char == ",":
            if buffer:
                # print("append")
                package.append(int(buffer))
                buffer = ""
        elif char == "[":
            # print("nested")
            nested, i = parse_package(package_string, i+1)
            package.append(nested)
        elif char == "]":
            if buffer:
                package.append(int(buffer))
            # print(f"returning", package)
            return package, i
        else:
            # number
            buffer += char
            # print("add 2 buffer", buffer)
        # next character
        i += 1
    
    print("error: parsing")
    return package, i

def check_order(left_package, right_package, debug=True, indent=""):
    """ check order results:
    -1 -> not in order (right is lower)
     0 -> can't order, continue
     1 -> in order (left is lower)
    """        
    while True:
        # check for empty packages
        if len(left_package) == 0:
            if debug:
                print(f"{indent}  - Left side ran out of items, so inputs are in the right order")
            return 1
        if len(right_package) == 0:
            if debug:
                print(f"{indent}  - Right side ran out of items, so inputs are not in the right order")
            return -1    
        left = left_package.pop(0)
        right = right_package.pop(0)
        if debug:
            print(f"{indent}- Compare {left} vs {right}")
        # check for Mixed types
        if isinstance(left, list) and isinstance(right, int):
            right = [right]
            if debug:
                print(f"{indent}  - Mixed types; convert right to {right} and retry comparison")
            # nested comparison:
            result = check_order(left, right, debug, indent+"  ")
            if result:
                return result
        # TODO: add left convertion to list
        # TODO: change to only compare if integers
        # compare 
        if left < right:
            if debug:
                print(f"{indent}  - Left side is smaller, so inputs are in the right order")
            return 1
        if right < left:
            if debug:
                print(f"{indent}  - Right side is smaller, so inputs are not in the right order")
            return -1
    return 0

def package_order():
    # read input file
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = ifp.read().rstrip()
    # print(data)
    
    ## split pair packages
    package_pairs = data.split("\n\n")
    # process each pair
    for i, pair in enumerate(package_pairs[:2]):
        print(f"== Pair {i} ==")
        package_pair = [parse_package(package)[0] for package in pair.split("\n")]
        print(f"comparing {package_pair[0]} vs {package_pair[1]}")
        check_order(package_pair[0], package_pair[1])
        print("-----")
        # for 
        


if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description='Day x Puzzle 1')
    _parser.add_argument('-i', '--input', help='Puzzle input')
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        package_order()
