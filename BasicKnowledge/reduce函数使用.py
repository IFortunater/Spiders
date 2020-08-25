#%%  --------------   用reduce做累加运算   ----------------
from functools import reduce


def add(x, y):
    return x + y


if __name__ == '__main__':
    r = reduce(add, [1, 2, 3, 4, 5])
    print(r)