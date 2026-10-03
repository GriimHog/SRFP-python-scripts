from typing import Tuple

names: tuple[str, ...] = tuple(x for x in input("Enter names : ").split(" "))
print(names)


def wordcnt(namelst):
    cnt = 0
    for n in namelst:
        if len(n) >= 5:
            cnt += 1
    print(cnt)


wordcnt(names)
