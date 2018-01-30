L = [2 ** x for x in range(7)]
X = 5

for i in L:
    if 2 ** X == i:
        print('at index', L.index(i))
        break
else:
    print(X, 'not found')