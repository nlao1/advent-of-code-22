from typing import Generator

def parse_input(filename: str) -> Generator[str, None, None]: # a-b,c-d -> (a, b, c, d)
    with open(filename, 'r') as f:
        for line in f:
            x, y = line.split(',')
            xs, xf = x.split('-')
            ys, yf = y.split('-')
            yield map(lambda x: int(x), (xs, xf, ys, yf))