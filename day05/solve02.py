import argparse
import re

def print_state(state):
    for i, x in enumerate(state):
        print(i+1, x)

def move_crates():
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = ifp.read().rstrip().split("\n\n")
    state = data[0].split("\n")

    # moves
    moves = []
    regex = re.compile(r"move (\d+) from (\d+) to (\d+)")
    for move in data[1].split("\n"):
        result = regex.search(move)
        moves.append((
            int(result.groups()[0]),
            int(result.groups()[1])-1,
            int(result.groups()[2])-1,
        ))
    # state
    state.reverse()
    number = len(state[0].strip().split("   "))
    stacks = [[] for _ in range(number)]
    for line in state[1:]:
        for i in range(number):
            crate = line[i*4+1]
            if crate != " ":
                stacks[i].append(crate)

    for move in moves:
        crane = []
        # get crates on a buffer
        for _ in range(move[0]):
            crane.append(stacks[move[1]].pop())
        crane.reverse()
        for x in crane:
            stacks[move[2]].append(x)
    
    ## get top crates
    top = []
    for stack in stacks:
        top.append(stack[-1])
    print(''.join(top))


if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description='Day x Puzzle 1')
    _parser.add_argument('-i', '--input', help='Puzzle input')
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        move_crates()
