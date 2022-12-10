import argparse

def execute_program():
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data_stack = ifp.read().rstrip().split("\n")

    signal_strength = []
    target_cycle = 20
    cycle = 0
    register_x = 1
    while len(data_stack) > 0:
        cycle += 1
        # remove first inscrution from stack
        instruction = data_stack.pop(0).split(" ")

        # "calculate" signal strength during cycle
        if cycle == target_cycle:
            signal_strength.append(register_x)
            target_cycle += 40
        
        if instruction[0] == "addx":
            # add instruction to simulate add duration
            data_stack.insert(0, f"rstx {instruction[1]}")
        if instruction[0] == "rstx":
            # Add result to register
            register_x += int(instruction[1])
        if instruction[0] == "noop":
            pass

        # print(f"cycle={cycle}\t instruction={instruction}\t register_x={register_x}")

    cycle = 20
    sum_signal_strength = 0
    for x in signal_strength:
        # print(f"{cycle} * {x} = {cycle*x}")
        sum_signal_strength += cycle * x
        cycle += 40
    print("Sum signal strength:", sum_signal_strength)

if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description='Day x Puzzle 1')
    _parser.add_argument('-i', '--input', help='Puzzle input')
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        execute_program()
