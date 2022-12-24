import argparse

def debug_print(trees, row, column):
    tree_height = trees[row][column]
    trees[row][column] = "X"
    for x in trees:
        for j in x:
            print(j, end="")
        print()
    trees[row][column] = tree_height

def count_visable():
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = ifp.read().rstrip().split("\n")
    trees = []
    for x in data:
        trees.append([int(y) for y in x])

    scenic_score = 0
    for row in range(len(trees)):
        for column in range(len(trees[0])):
            if column == 0 or column == len(trees[0])-1:
                # edge tree, ignore for calculations
                continue
            if row == 0 or row == len(trees)-1:
                # edge tree, ignore for calculations
                continue

            tree_check = trees[row][column]
            tree_score = 1
            # check up
            visable_trees = 0
            for x in range(1, row+1):
                visable_trees += 1
                if trees[row-x][column] >= tree_check:
                    # same height, view blocked
                    break
            # multiply score
            tree_score *= visable_trees

            # check left
            visable_trees = 0
            for x in range(1, column+1):
                visable_trees += 1
                if trees[row][column-x] >= tree_check:
                    # same height, view blocked
                    break
            # multiply score
            tree_score *= visable_trees

            # check right
            visable_trees = 0
            for x in range(1, len(trees)-column):
                visable_trees += 1
                if trees[row][column+x] >= tree_check:
                    # same height, view blocked
                    break
            # multiply score
            tree_score *= visable_trees

            # check down
            visable_trees = 0
            for x in range(1, len(trees[0])-row):
                visable_trees += 1
                if trees[row+x][column] >= tree_check:
                    # same height, view blocked
                    break
            # multiply score
            tree_score *= visable_trees

            # check max
            scenic_score = max(scenic_score, tree_score)
    print("max scenic score:", scenic_score)

if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description="Day 8 Puzzle 2")
    _parser.add_argument("-i", "--input", help="Puzzle input")
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        count_visable()
