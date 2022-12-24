import argparse
import logging

def falling_sand():
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = ifp.read().rstrip().split("\n")

    # get window sizes
    x_min = 500
    x_max = 500
    y_max = 0
    cavern_rocks = []
    for line in data:
        rocks = []
        for pos in line.split(" -> "):
            x, y = pos.split(",")
            rocks.append((int(x), int(y)))
            x_min = min(x_min, int(x))
            x_max = max(x_max, int(x))
            y_max = max(y_max, int(y))
        cavern_rocks.append(rocks)

    # oversize cavern
    oversize = 150
    cavern_left_pos = x_min-oversize
    x_max += oversize
    y_max += 1
    # create slice of cavern with +2 columns and +1 row
    cavern = [["."]*(x_max-cavern_left_pos+1) for _ in range(y_max+1)]
    cavern[0][500-cavern_left_pos] = "+"
    # add floor
    cavern.append(["#"]*(x_max-cavern_left_pos+1))

    # draw rocks
    for rocks in cavern_rocks:
        for i in range(len(rocks)-1):
            logging.debug(f"{rocks[i]}, {rocks[i+1]}")
            if rocks[i][0] == rocks[i+1][0]:
                # vertical rock line
                y_min = min(rocks[i][1], rocks[i+1][1])
                y_max = max(rocks[i][1], rocks[i+1][1])
                # draw line
                for j in range(y_min, y_max+1):
                    cavern[j][rocks[i][0]-cavern_left_pos] = "#"
            else:
                # horizontal rock line
                x_min = min(rocks[i][0], rocks[i+1][0])
                x_max = max(rocks[i][0], rocks[i+1][0])
                # draw line
                for j in range(x_min, x_max+1):
                    cavern[rocks[i][1]][j-cavern_left_pos] = "#"


    sand_at_rest = 0
    sand_row = 0
    sand_column = 500-cavern_left_pos
    # pour infinite sand
    while True:
        # check if down is air
        if cavern[sand_row+1][sand_column] == ".":
            # update cavern
            cavern[sand_row][sand_column] = "."
            cavern[sand_row+1][sand_column] = "o"
            #move down
            sand_row += 1


        # check if down and left
        elif cavern[sand_row+1][sand_column-1] == ".":
            # update cavern
            cavern[sand_row][sand_column] = "."
            cavern[sand_row+1][sand_column-1] = "o"
            # move down left
            sand_row += 1
            sand_column -= 1

        # check if down and right
        elif cavern[sand_row+1][sand_column+1] == ".":
            # update cavern
            cavern[sand_row][sand_column] = "."
            cavern[sand_row+1][sand_column+1] = "o"
            # move down right
            sand_row += 1
            sand_column += 1

        else:
            # sand at rest
            sand_at_rest += 1

            if sand_row == 0 and sand_column == 500-cavern_left_pos:
                # sand cover spout, breaking loop
                break
            # pour new sand
            logging.debug("new sand")
            sand_row = 0
            sand_column = 500-cavern_left_pos

        if sand_row == len(cavern)-1:
            # sand falling to abyss, break while loop and throw error
            raise Exception("floor too small, sand falled into abyss")

        if logging.root.level <= logging.DEBUG:
            logging.debug(f"sand_at_rest: {sand_at_rest}")
            for line in cavern:
                logging.debug(f"{('').join(line)}")
            input()

    if logging.root.level <= logging.INFO:
        for line in cavern:
                logging.info(f"{('').join(line)}")

    print("Sand before falling to abyss:", sand_at_rest)


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
        falling_sand()
