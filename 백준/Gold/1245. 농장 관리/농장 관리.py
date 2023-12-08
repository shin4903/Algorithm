from collections import deque
dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [1, -1, 0, 1, -1, 0, 1, -1]
def bfs(x,y):
    global result
    visited = [[0] * M for _ in range(N)]
    q = deque([])
    q.append((x,y))
    while q:
        x, y = q.popleft()
        if not visited[x][y]:
            visited[x][y] = 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] and not visited[nx][ny]:
                if arr[nx][ny] > arr[x][y]:
                    return
                elif arr[nx][ny] == arr[x][y]:
                    visited[nx][ny] = 1
                    visited2[nx][ny] = 1
                    q.append((nx,ny))
                elif arr[nx][ny] < arr[x][y]:
                    visited[nx][ny] = 1
                    continue
    result += 1
    return

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited2 = [[0] * M for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if not visited2[i][j]:
            bfs(i,j)
print(result)