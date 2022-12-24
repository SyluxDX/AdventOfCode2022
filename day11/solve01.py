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

def monkey_keep_away():
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
    for _ in range(20):
        # monkey turn
        for i, monkey in enumerate(monkeys_list):
            monkey: Monkey
            # print("Monkey", i)
            while monkey.items:
                old = monkey.items.pop(0)
                # increment inspections
                monkey.inspections += 1
                # increase worry by inpecting it
                new = eval(monkey.operation)
                # decrease worry since item not broken
                final = new//3
                # choose target of throw
                if not final%monkey.test_division:
                    monkeys_list[monkey.throw_true].items.append(final)
                else:
                    monkeys_list[monkey.throw_false].items.append(final)

    interactions = []
    for i, monkey in enumerate(monkeys_list):
        # print(f"Monkey {i} inspected items {monkey.inspections} times.")
        interactions.append(monkey.inspections)

    interactions.sort()
    print(f"Level of monkey bussiness: {interactions[-1]*interactions[-2]}")


if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description="Day 11 Puzzle 1")
    _parser.add_argument("-i", "--input", help="Puzzle input")
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        monkey_keep_away()
