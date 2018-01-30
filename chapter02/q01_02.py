S = 'Hello world!'

tmp = 0
for x in S:
    tmp += ord(x)

print('The total number of {0:s} is {1:d}'.format(S, tmp))