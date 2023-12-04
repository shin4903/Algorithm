import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arr.sort()
s = arr[0][0]
e = arr[0][1]
result = 0
for i in range(1, N):
    if s <= arr[i][0] <= e and e <= arr[i][1]:
        e = arr[i][1]
    elif e < arr[i][0]:
        result += e-s
        s = arr[i][0]
        e = arr[i][1]
result += e-s
print(result)