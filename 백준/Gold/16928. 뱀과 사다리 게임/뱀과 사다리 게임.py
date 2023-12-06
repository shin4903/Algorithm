def bfs(s):
    q = [s]
    while q:
        s = q.pop(0)
        for i in range(1,7):
            ns = s + i
            if 1 <= ns <= 100:
                if game[ns] == 1:
                    for ladder in L:
                        if ns == ladder[0] and not visited[ladder[1]]:
                            visited[ladder[1]] = visited[s] + 1
                            if ladder[1] == 100 :
                                return
                            if ladder[1] != 100 :
                                q.append(ladder[1])

                elif game[ns] == 2:
                    for snake in S:
                        if ns == snake[0] and not visited[snake[1]]:
                            visited[snake[1]] = visited[s] + 1
                            if snake[1] != 100:
                                q.append(snake[1])
                            elif snake[1] == 100:
                                return 
                elif game[ns] == 0:

                    if not visited[ns]:
                        visited[ns] = visited[s] + 1
                        if ns == 100:
                            return
                        if ns != 100:
                            q.append(ns)
    return
N, M = map(int,input().split())
L = []
S = []
game = [0] * 101
visited = [0] * 101
visited[1] = 0
result = []
for _ in range(N):
    l = list(map(int,input().split()))
    L.append(l)
    game[l[0]] = 1
for _ in range(M):
    s = list(map(int,input().split()))
    S.append(s)
    game[s[0]] = 2

bfs(1)
print(visited[100])