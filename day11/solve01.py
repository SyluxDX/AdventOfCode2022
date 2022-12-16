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
    # for _ in range(20):
    for _ in range(1):
        # monkey turn
        for i, monkey in enumerate(monkeys_list):
            monkey: Monkey
            print("Monkey", i)
            while monkey.items:
                old = monkey.items.pop(0)
                # increment inspections
                monkey.inspections += 1
                print(" inspect item with", old)
                # increase worry by inpecting it
                new = eval(monkey.operation)
                print(" worry increase to", new)
                # decrease worry since item not broken
                final = new//3
                print(" monkey bored, worry", final)
                # choose target of throw
                if not final%monkey.test_division:
                    print(f" worry divisable by {monkey.test_division}, throw to {monkey.throw_true}")
                    monkeys_list[monkey.throw_true].items.append(final)
                else:
                    # print(monkey.throw_false)
                    print(f" worry not divisable by {monkey.test_division}, throw to {monkey.throw_false}")
                    monkeys_list[monkey.throw_false].items.append(final)
                print()
    #monkey steps
    #for each item
    # inspect item: increase worry by operation
    # worry decrease by divide by 3 round down
    # test worry
    # throw item to another monkey
    

if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description='Day x Puzzle 1')
    _parser.add_argument('-i', '--input', help='Puzzle input')
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        monkey_keep_away()
