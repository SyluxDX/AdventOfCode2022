import argparse

def exewcute_and_draw():
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data_stack = ifp.read().rstrip().split("\n")

    screen = []
    line_buffer = []
    target_cycle = 40
    cycle = 0
    register_x = 1
    crt_row = 0
    while len(data_stack) > 0:
        cycle += 1
        # remove first inscrution from stack
        instruction = data_stack.pop(0).split(" ")

        # draw sprite pixel during cycle
        sprite = [register_x-1, register_x, register_x+1]
        if crt_row in sprite:
            line_buffer.append("#")
        else:
            line_buffer.append(".")
        crt_row += 1
        if cycle == target_cycle:
            screen.append(line_buffer)
            line_buffer = []
            crt_row = 0
            target_cycle += 40
        
        if instruction[0] == "addx":
            # add instruction to simulate add duration
            data_stack.insert(0, f"rstx {instruction[1]}")
        if instruction[0] == "rstx":
            # Add result to register
            register_x += int(instruction[1])
        if instruction[0] == "noop":
            pass

    # print screen
    for line in screen:
        print("".join(line))

if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description='Day x Puzzle 1')
    _parser.add_argument('-i', '--input', help='Puzzle input')
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        exewcute_and_draw()
