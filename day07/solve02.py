import argparse

def device_usage():
    with open(ARGS.input, "r", encoding="utf8")as ifp:
        data = ifp.read().rstrip().split("\n")

    folder_size = {}
    path = []
    for line in data:
        sline = line.split(" ")
        if sline[0] == "$":
            if sline[1] == "cd":
                if sline[2] == "..":
                    path.pop()
                else:
                    path.append(sline[2])
            if sline[1] == "ls":
                pass
        else:
            # assuming a ls was called
            if sline[0] == "dir":
                pass
            else:
                aux_path = []
                for folder in path:
                    aux_path.append(folder)
                    key_folder = "/".join(aux_path)
                    if key_folder in folder_size:
                        folder_size[key_folder] += int(sline[0])
                    else:
                        folder_size[key_folder] = int(sline[0])

    root = folder_size["/"]
    free = 70000000 - root
    need = 30000000 - free

    clear_folder = ""
    clear_size = root
    for folder, size in folder_size.items():
        if size > need and size <= clear_size:
            clear_size = size
            clear_folder = folder
    print(f"Delete folder {clear_folder}, freeing {clear_size}")


if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description="Day 7 Puzzle 2")
    _parser.add_argument("-i", "--input", help="Puzzle input")
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        device_usage()
