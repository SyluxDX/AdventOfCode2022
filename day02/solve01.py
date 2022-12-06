import argparse

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
rps_play = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}
rps_points = {
    "win": 6,
    "draw": 3,
    "loss": 0,
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

def rps_game(play1, play2):
    if play1 == play2:
        return "draw"
    if play1 == "rock":
        if play2 == "scissors":
            return "win"
        else:
            return "loss"
    
    if play1 == "paper":
        if play2 == "rock":
            return "win"
        else:
            return "loss"
    
    if play1 == "scissors":
        if play2 == "paper":
            return "win"
        else:
            return "loss"


def follow_strategy():
    with open(ARGS.input, "r", encoding="utf8") as ifp:
        input_data = ifp.read().strip()
    plays = [x.split(" ") for x in input_data.split("\n")]
    total_points = 0
    for play in plays:
        pl1 = rps_play[play[0]]
        pl2 = rps_play[play[1]]

        points = rps_points[pl2] + rps_points[rps_game(pl2, pl1)]
        total_points += points

    print(f"Total points: {total_points}")


if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description='Day x Puzzle 1')
    _parser.add_argument('-i', '--input', help='Puzzle input')
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        follow_strategy()
    a = list()
