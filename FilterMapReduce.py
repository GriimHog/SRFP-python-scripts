from functools import reduce
from typing import Any

numbers: list[str] = input("enter number : ").split(" ")
evens: tuple[int, ...] = tuple(filter(lambda n: n % 2 == 0, tuple(int(x) for x in numbers)))
doubles: tuple[int | Any, ...] = tuple(map(lambda n: 2 * n, evens))
sumd: int | Any = reduce(lambda a, b: a + b, doubles)
print("Number of even numbers are : {} and doubles of them are : {} and their sum is : {}".format(len(evens), doubles,
                                                                                                  sumd))
