
def adder(good, bad, ugly, **kwargs):
    tmp = good + bad + ugly
    for k in kwargs.keys():
        tmp += kwargs[k]
    return tmp




