N = int(input())
data = list(map(int,input().split()))
stack = []
result = [0 for _ in range(N)]
for i in range(N):
    while stack:
        if stack[-1][1] > data[i]:
            result[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i,data[i]])
print(*result)