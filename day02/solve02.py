import argparse

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
rps_play = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "loss",
    "Y": "draw",
    "Z": "win",
}
rps_points = {
    "win": 6,
    "draw": 3,
    "loss": 0,
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

def rps_game(adversary, result):
    if result == "draw":
        return adversary
    
    if result == "win":
        if adversary == "rock":
            return "paper"
        elif adversary == "paper":
            return "scissors"
        else:
            return "rock"
    
    if result == "loss":
        if adversary == "rock":
            return "scissors"
        elif adversary == "paper":
            return "rock"
        else:
            return "paper"

def follow_strategy():
    with open(ARGS.input, "r", encoding="utf8") as ifp:
        input_data = ifp.read().strip()
    strategies = [x.split(" ") for x in input_data.split("\n")]
    total_points = 0
    for strategy in strategies:
        adv_play = rps_play[strategy[0]]
        result = rps_play[strategy[1]]
        
        points = rps_points[result] + rps_points[rps_game(adv_play, result)]
        total_points += points

    print(f"Total points: {total_points}")


if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description="Day 2 Puzzle 2")
    _parser.add_argument("-i", "--input", help="Puzzle input")
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        follow_strategy()
    a = list()
