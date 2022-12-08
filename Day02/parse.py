from typing import Generator

def parse_input(filename: str) -> Generator[str, None, None]:
    with open(filename) as f:
        for line in f:
            yield line.strip().split(' ')