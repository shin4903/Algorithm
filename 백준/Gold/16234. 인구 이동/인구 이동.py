import sys
from collections import deque
def bfs(i,j):
    q = deque([])
    q.append((i,j))
    data = [[i,j]]
    sumData = arr[i][j]
    while q:
        x, y = q.popleft()
        if not visited[x][y]:
            visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                    visited[nx][ny] = 1
                    data.append([nx,ny])
                    q.append((nx,ny))
                    sumData += arr[nx][ny]
    for d in data:
        x,y = d[0], d[1]
        arr[x][y] = sumData // len(data)
    return


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, L, R = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
result = 0
while True:
    visited = [[0] * N for _ in range(N)]
    flag = False
    for x in range(N):
        for y in range(N):
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and not visited[x][y]:
                    if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                        visited[x][y] = 1
                        bfs(x,y)
                        flag = True
    if not flag:
        break
    result += 1
print(result)