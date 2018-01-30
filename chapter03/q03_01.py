from functools import reduce


def adder(*args, **kwargs):
    return reduce(lambda x, y: x+y, args)