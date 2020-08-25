# %%    --------------   单参数map函数的使用   ---------------
def func(x):
    return x * x


if __name__ == '__main__':
    r = map(func, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(r))


# %%    --------------   多参数map函数的使用   ---------------
def func(x, y):
    return x ** 2 + y ** 2


if __name__ == '__main__':
    r = map(func, [1, 2, 3], [1, 2, 3])
    print(list(r))


# %%    --------------   小练习测试   ---------------
def normalize(name):
    return name.title()


if __name__ == '__main__':
    l1 = ['LIsa', 'BaRt', 'tom']
    print(list(map(normalize, l1)))
