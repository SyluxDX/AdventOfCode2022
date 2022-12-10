import argparse

# dataclass
class Position:
    x = 0
    y = 0
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def __str__(self):
        return f"(x={self.x}, y={self.y})"
    def pos(self):
        return (self.x, self.y)

def print_map(head, tail, size=(5, 6), start=(4,0)):
    map = [["."]*size[1] for _ in range(size[0])]
    # add start
    map[start[0]][start[1]] = "s"
    # add tail
    map[tail.x][tail.y] = "T"
    # add head
    map[head.x][head.y] = "H"

    for line in map:
        print("".join(line))

def tail_head_touching(head, tail):
    eulc_x = abs(head.x-tail.x)
    eulc_y = abs(head.y-tail.y)
    return eulc_x <= 1 and eulc_y <= 1

def simulate_rope_snake():
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = [line.split(" ") for line in ifp.read().rstrip().split("\n")]

    head = Position(4,0)
    tail = Position(4,0)
    translate_move = {
        "R": (0,1),
        "U": (-1,0),
        "L": (0,-1),
        "D": (1,0),
    }
    # set of positons
    visited_by_tail = {tail.pos()}

    # print("== Initial state == ")
    # print_map(head, tail)
    for motion in data:
        # print(f"== {motion[0]} {motion[1]} ==")
        move = translate_move[motion[0]]
        for _ in range(int(motion[1])):
            past_head = head.pos()
            # move head
            head.x += move[0]
            head.y += move[1]
            # check if head and tail not touching
            if not tail_head_touching(head, tail):
                # move tail to past position of head
                tail.x = past_head[0]
                tail.y = past_head[1]
                visited_by_tail.add(tail.pos())

        #     print_map(head, tail)
        #     input()        
        # print()
    print("Tail visited:", len(visited_by_tail))


if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description='Day x Puzzle 1')
    _parser.add_argument('-i', '--input', help='Puzzle input')
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        simulate_rope_snake()
