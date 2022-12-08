from typing import List

def parse_input(filename) -> List[int]:
    res = []
    with open(filename) as f:
        sum = 0
        for line in f:
            if str.isspace(line):
                res.append(sum)
                sum = 0
            else:
                sum += int(line)
    return res