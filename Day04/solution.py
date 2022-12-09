from parse import parse_input
from typing import List, Tuple
import itertools

def solution_pt1(l: List[Tuple[int, int, int, int]]) -> int:
    count = 0
    for xs, xf, ys, yf in l:
        if (xs <= ys and xf >= yf) or (ys <= xs and yf >= xf):
            count += 1
    return count

def solution_pt2(l: List[Tuple[int, int, int, int]]) -> int:
    count = 0
    for xs, xf, ys, yf in l:
        if (xs <= ys and xf >= ys) or (ys <= xs and yf >= xs):
            count += 1
    return count

# print(solution_pt1(parse_input('example.txt')))
# print(solution_pt1(parse_input('input.txt')))
# print(solution_pt2(parse_input('example.txt')))
# print(solution_pt2(parse_input('input.txt')))