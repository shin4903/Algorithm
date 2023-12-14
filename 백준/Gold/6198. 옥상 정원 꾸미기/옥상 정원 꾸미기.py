import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
result = 0
stack = []
for i in range(N):
    while stack:
        if arr[i] >= stack[-1]:
            stack.pop()
        else:
            result += len(stack)
            break
    stack.append(arr[i])

print(result)