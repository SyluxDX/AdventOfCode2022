import argparse

def count_visable():
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = ifp.read().rstrip().split("\n")
    trees = []
    for x in data:
        trees.append([int(y) for y in x])

    count_visable = 0
    for row in range(len(trees)):
        for column in range(len(trees[0])):
            if column == 0 or column == len(trees[0])-1:
                count_visable += 1
                continue
            if row == 0 or row == len(trees)-1:
                count_visable += 1
                continue
            tree_check = trees[row][column]
            # check up
            visable = True
            for x in range(1, row+1):
                if trees[row-x][column] >= tree_check:
                    visable = False
            if visable:
                count_visable += 1
                continue

            # check left
            visable = True
            for x in range(1, column+1):
                if trees[row][column-x] >= tree_check:
                    visable = False
            if visable:
                count_visable += 1
                continue

            # check right
            visable = True
            for x in range(1, len(trees)-column):
                if trees[row][column+x] >= tree_check:
                    visable = False
            if visable:
                count_visable += 1
                continue

            # check down
            visable = True
            for x in range(1, len(trees[0])-row):
                if trees[row+x][column] >= tree_check:
                    visable = False
            if visable:
                count_visable += 1
                continue
    print("visable trees:", count_visable)

if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description="Day 8 Puzzle 1")
    _parser.add_argument("-i", "--input", help="Puzzle input")
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        count_visable()
