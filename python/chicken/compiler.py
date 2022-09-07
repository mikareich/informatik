from builtins import print


def chicken_to_minichicken(code: str) -> str:
    res = []
    code = code.lower()
    for l in code.split("\n"):
        res.append(str(l.count("chicken")))
    return " ".join(res)

def minichicken_to_chicken(code: str) -> str:
    res = []
    for n in code.split():
        res.append(" ".join("chicken" for _ in range(int(n))))
    return "\n".join(res)

print(minichicken_to_chicken('hello world'))