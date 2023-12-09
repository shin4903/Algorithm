dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
result = 0
data = []
dp = [[1] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        data.append([arr[i][j],i,j])
data.sort()
for i in data:
    value = i[0]
    x = i[1]
    y = i[2]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and value < arr[nx][ny]:
            dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)

for i in dp:
    result = max(result, max(i))
print(result)