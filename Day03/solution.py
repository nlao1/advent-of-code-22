from parse import parse_input
from typing import Optional, Generator

def priority(char: str) -> Optional[int]:
    if str.isupper(char):
        return ord(char) - ord('A') + 27
    elif str.islower(char):
        return ord(char) - ord('a') + 1
    return None

def solution_pt1(filename: str) -> int:
    result = 0
    for line in parse_input(filename):
        first = set(line[0])
        second = set(line[1])
        intersection = first.intersection(second)
        for x in intersection:
            result += priority(x)
    return result

def solution_pt2(filename: str) -> int:
    result = 0
    group = []
    for line in parse_input(filename):
        if len(group) < 3:
            group.append(line)
        if len(group) == 3:
            first = set(group[0][0] + group[0][1])
            second = set(group[1][0] + group[1][1])
            third = set(group[2][0] + group[2][1])
            common = first.intersection(second, third)
            for x in common:
                result += priority(x)
            group = []
    return result

# print(solution_pt1('example.txt'))
# print(solution_pt1('input.txt'))
# print(solution_pt2('example.txt'))
print(solution_pt2('input.txt'))