import argparse

# dataclass
class Monkey:
    def __init__(self, items, operation, test_division, throw_true, throw_false) -> None:
        self.items = items
        self.operation = operation
        self.test_division = test_division
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.inspections = 0
    def __str__(self) -> str:
        return """items: {}
op: new: {}
test: //{}
if true throw to: {}
if false throw to: {}""".format(
    self.items,
    self.operation,
    self.test_division,
    self.throw_true,
    self.throw_false
)

def monkey_keep_away(debug=False):
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = ifp.read().rstrip()
    monkeys_list = []
    for monkey_block in data.split("\n\n"):
        monkey_operations = [line.strip() for line in monkey_block.split("\n")]
        monkeys_list.append(Monkey(
            # monkey id
            # monkey_operations[0][7:-1],
            # items
            [int(n) for n in monkey_operations[1][16:].split(", ")],
            # inspect operation
            monkey_operations[2][17:],
            # throw select test
            int(monkey_operations[3][19:]),
            # throw option if true
            int(monkey_operations[4][25:]),
            # throw option if false
            int(monkey_operations[5][26]),
        ))

    # calculate Least Common Multiple for monkeys division throw test
    # since test-division are all prime number it can be calculated by multiplication
    monkey_lcm = 1
    for monkey in monkeys_list:
        monkey_lcm *= monkey.test_division

    debug_round = [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    for round in range(10000):
        # print(round)
        # monkey turn
        for i, monkey in enumerate(monkeys_list):
            monkey: Monkey
            while monkey.items:
                old = monkey.items.pop(0)
                # increment inspections
                monkey.inspections += 1
                # increase worry by inpecting it
                new = eval(monkey.operation)
                # Manage worry
                final = new % monkey_lcm
                # choose target of throw
                if not final%monkey.test_division:
                    monkeys_list[monkey.throw_true].items.append(final)
                else:
                    monkeys_list[monkey.throw_false].items.append(final)
        ## debug rounds
        if debug and round+1 in debug_round:
            print(f"== After round {round+1} ==")
            for i, monkey in enumerate(monkeys_list):
                print(f"Monkey {i} inspected items {monkey.inspections} times.")

    interactions = []
    for i, monkey in enumerate(monkeys_list):
        # print(f"Monkey {i} inspected items {monkey.inspections} times.")
        interactions.append(monkey.inspections)

    interactions.sort()
    print(f"Level of monkey bussiness: {interactions[-1]*interactions[-2]}")


if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description="Day 11 Puzzle 2")
    _parser.add_argument("-i", "--input", help="Puzzle input")
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        monkey_keep_away()
