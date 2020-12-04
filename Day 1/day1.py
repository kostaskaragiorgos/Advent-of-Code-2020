"""
Specifically, they need you to find the two entries that
 sum to 2020 and then multiply those two numbers together.
"""

TEST = [
1721,
979,
366,
299,
675,
1456
]

from typing import List

def find_product(numbers: List[int]) -> int:
    for i in numbers:
        for j in numbers:
            if int(i)+int(j)== 2020:
                return int(i) * int(j)


def find_product2(numbers: List[int]) -> int:
    for i in numbers:
        for j in numbers:
            for x in numbers:
                if int(i)+int(j)+ int(x)== 2020:
                    return int(i) * int(j) * int(x)


with open("day1.txt") as f:
    lines = f.read().split("\n")
    print(find_product(lines))
    print(find_product2(lines))


    