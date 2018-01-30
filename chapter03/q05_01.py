def copyDict(**kwargs):
    res = dict()
    for key in kwargs.keys():
        res[key] = kwargs[key]
    return res

if __name__ == '__main__':
    tmp = copyDict(a=1, b=2, c=3)