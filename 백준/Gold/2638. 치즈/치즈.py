import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0

def check(): # 치즈가 있는지 없는지 확인
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                return True
    return False

def bfs():
    q = deque([])
    q.append((0,0))
    visited = [[0] * M for _ in range(N)]
    cheese = [[0] * M for _ in range(N)]
    while q:
        x, y = q.popleft()
        if not visited[x][y]:
            visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
            elif 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                cheese[nx][ny] += 1
    return cheese

while check():
    cheese = bfs()
    for i in range(N):
        for j in range(M):
            if cheese[i][j] >= 2:
                arr[i][j] = 0
    result += 1
print(result)