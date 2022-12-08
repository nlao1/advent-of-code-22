from parse import parse_input

parsed_input = parse_input("input.txt")
def solution_pt1():
    return max(parsed_input)

def solution_pt2():
    return sum(sorted(parsed_input, reverse=True)[:3])

print(solution_pt1())
print(solution_pt2())
