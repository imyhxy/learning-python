D = {'who': 'is', 'me': '?', 'i': 'dont', 'know': 'what', 'to': 'say'}

tmp = list(D.keys())
tmp.sort()
for x in tmp:
    print(x, '==>', D[x])
