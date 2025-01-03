import logging
from math import sqrt
from random import randint
from typing import Tuple


def quadratic_equation(a: int, b: int, c: int) -> Tuple[float]:
    def qa(text: str):
        return f"quadratic_equation:\t{text}\n"

    d = b**2 - 4 * a * c
    logging.debug(qa("a: {0}, b: {1}, c: {2}".format(a, b, c)))
    try:
        sq = sqrt(d)
    except Exception as exc:
        logging.debug(qa("Exception: {0}".format(str(exc))))
    else:
        logging.debug(qa("Discriminant square root: {0}".format(sq)))
        x1 = -b + sq / (2 * a)
        x2 = -b - sq / (2 * a)
        logging.debug(qa("x1: {0}, x2: {1}".format(x1, x2)))

        return x1, x2


def rnd(a: int = -10, b: int = 10) -> int:
    return randint(a, b)


equations = [(rnd(), rnd(), rnd()) for _ in range(10)]

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    for values in equations:
        print("Values\t a: {0}, b: {1}, c: {2}".format(*values))
        print("Result\t x1: {0}, x2: {1}".format(*quadratic_equation(*values)))
