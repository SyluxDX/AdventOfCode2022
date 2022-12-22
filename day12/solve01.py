import argparse

def convert_height(letter_height):

    start = None
    end = None
    split = letter_height.split("\n")
    rows = len(split)
    columns = len(split[0])

    height = [[None for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            cell = split[i][j]
            if cell == "S":
                start = (i, j)
                cell = "a"
            if cell == "E":
                end = (i, j)
                cell = "z"
            # ord("a") = 97
            height[i][j] = ord(cell) - 97

    return height, start, end

def debug_print(path_taken, newline=True):
    if newline:
        print()
    for x in path_taken:
        print("".join(x))

def bfs_path_finding(map, start, end):
    pass

def hill_climb():
    ## Get map
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = ifp.read().rstrip()
    print(data)
    height, start, end = convert_height(data)

    for x in height:
        print(x)
    
    ## Get debug map
    path_taken = [["."]*len(height[0]) for _ in range(len(height))]
    path_taken[start[0]][start[1]] = "S"
    path_taken[end[0]][end[1]] = "E"

    debug_print(path_taken)


if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description='Day x Puzzle 1')
    _parser.add_argument('-i', '--input', help='Puzzle input')
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        hill_climb()
