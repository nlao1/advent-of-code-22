from typing import Generator

def parse_input(filename: str) -> Generator[str, None, None]:
    with open(filename) as f:
        for line in f:
            line = line.strip()
            yield (line[:len(line) // 2], line[len(line) // 2:])