import sys
T = int(sys.stdin.readline())

for _ in range(T):
    P = input()
    result = []
    tmp = []
    for p in P:
        if p == '<':
            if result:
                tmp.append(result.pop())
        elif p == '>':
            if tmp:
                result.append(tmp.pop())
        elif p == '-':
            if result:
                result.pop()
        else:
            result.append(p)
    while tmp:
        result.append(tmp.pop())
    print(''.join(result))