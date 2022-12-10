import argparse

# dataclass
class KnotPosition:
    knot_repr = "x"
    x = 0
    y = 0
    def __init__(self, x, y, knot_repr) -> None:
        self.x = x
        self.y = y
        self.knot_repr = knot_repr
    def __str__(self):
        return f"({self.knot_repr}: x={self.x}, y={self.y})"
    def pos(self):
        return (self.x, self.y)

def print_tail_map(tail_position, size=(5, 6), start=(4,0)):
    tail_map = [["."]*size[1] for _ in range(size[0])]
    # add tail trail
    for position in tail_position:
        tail_map[position[0]][position[1]] = "#"
    # add start
    tail_map[start[0]][start[1]] = "s"
    # print map
    for line in tail_map:
        print("".join(line))


def print_map(knots, size=(5, 6), start=(4,0)):
    map = [["."]*size[1] for _ in range(size[0])]
    # add start
    map[start[0]][start[1]] = "s"
    # add knots on reverse order:
    for knot in knots[::-1]:
        map[knot.x][knot.y] = knot.knot_repr

    for line in map:
        print("".join(line))

def knots_touching(first_knot, second_knot):
    eulc_x = abs(first_knot.x-second_knot.x)
    eulc_y = abs(first_knot.y-second_knot.y)
    return eulc_x <= 1 and eulc_y <= 1

def simulate_rope_snake():
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = [line.split(" ") for line in ifp.read().rstrip().split("\n")]

    # Create list of knots and overwrite knot zero as HEADER
    knot_list = [KnotPosition(4, 0, str(x)) for x in range(2)]
    knot_list = [KnotPosition(15, 11, str(x)) for x in range(10)]
    knot_list[0].knot_repr = "H"
    visited_by_tail = {knot_list[-1].pos()}
    translate_move = {
        "R": (0,1),
        "U": (-1,0),
        "L": (0,-1),
        "D": (1,0),
    }
    
    # print("== Initial state == ")
    # print_map(knot_list, (21,26), (15,11))
    for motion in data:
        # print(f"== {motion[0]} {motion[1]} ==")
        move = translate_move[motion[0]]
        for _ in range(int(motion[1])):
            # move head
            knot_list[0].x += move[0]
            knot_list[0].y += move[1]
            # propagate changes in knots
            for i in range(1, len(knot_list)):
                if knots_touching(knot_list[i], knot_list[i-1]):
                    # if knots are thouching the following are also
                    break
                else:
                    # calculate euclidean vector
                    elc_x = knot_list[i-1].x-knot_list[i].x
                    elc_y = knot_list[i-1].y-knot_list[i].y
                    vector_x = 0
                    vector_y = 0
                    if elc_x:
                        vector_x = elc_x//abs(elc_x)
                    if elc_y:
                        vector_y = elc_y//abs(elc_y)
                    # move knot
                    knot_list[i].x += vector_x 
                    knot_list[i].y += vector_y

            # add tail to set positions
            visited_by_tail.add(knot_list[-1].pos())

        # print_map(knot_list, (21,26), (15,11))
        # input()        
        # print()
    print("Tail visited:", len(visited_by_tail))
    # print_tail_map(visited_by_tail, (21,26), (15,11))

if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description='Day x Puzzle 1')
    _parser.add_argument('-i', '--input', help='Puzzle input')
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        simulate_rope_snake()
