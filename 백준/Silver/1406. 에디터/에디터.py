import sys
result = list(map(str,input()))
tmp = []
N = int(sys.stdin.readline())
for _ in range(N):
    command = sys.stdin.readline()
    if command[0] == 'L':
        if result:
            tmp.append(result.pop())
    elif command[0] == 'D':
        if tmp:
            result.append(tmp.pop())
    elif command[0] == 'B':
        if result:
            result.pop()
    elif command[0] == 'P':
        result.append(command[2])
if tmp:
    while tmp:
        result.append(tmp.pop())
print(''.join(result))