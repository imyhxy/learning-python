L = [2 ** x for x in range(7)]
X = 5
i = 0

while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    else:
        i += 1
else:
    print(X, 'not found')
    print(L)