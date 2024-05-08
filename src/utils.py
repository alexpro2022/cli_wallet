def parse(input: str) -> list[str]:
    inp: list[str] = list(map(lambda s: s.strip(), input.split("-")))
    if len(inp) == 1:
        inp.append("")
    return inp
