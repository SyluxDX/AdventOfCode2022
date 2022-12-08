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
                # print(f"{'|'.join(path)}\\{sline[1]}")
                pass
            else:
                aux_path = []
                for folder in path:
                    aux_path.append(folder)
                    key_folder = '/'.join(aux_path)
                    if key_folder in folder_size:
                        folder_size[key_folder] += int(sline[0])
                    else:
                        folder_size[key_folder] = int(sline[0])
        
        # print("cmd:", line)
        # print("path:", path)
        # print("size:", folder_size)
        # input()
    
    print("folders:")
    for key in folder_size:
        print(folder_size[key])
    
    print("folder size")
    sum_total = 0
    print("total", sum_total)
    for key in folder_size:
        # print(key, folder_size[key])
        if folder_size[key] < 100000:
            print(key, folder_size[key])
            sum_total += folder_size[key]
            print("t:", sum_total)
    print("total sum:", sum_total)


if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description='Day x Puzzle 1')
    _parser.add_argument('-i', '--input', help='Puzzle input')
    ARGS = _parser.parse_args()

    if not ARGS.input:
        print("No input argument, use flag -i")
    else:
        device_usage()
