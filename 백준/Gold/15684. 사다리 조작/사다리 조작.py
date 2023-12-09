def check():
    for start in range(1,N+1):
        now = start
        for j in range(1,H+1):
            if arr[j][now]:
                now += 1
            elif arr[j][now-1]:
                now -= 1
        if now != start:
            return False
    return True

def back(tmp, idx):
    global result
    if check():
        result = min(tmp, result)
        return
    if tmp >= 3 or tmp >= result:
        return

    for i in range(idx,len(data)):
        x,y = data[i][0], data[i][1]
        if not arr[x][y] and not arr[x][y-1] and not arr[x][y+1]:
            arr[x][y] = 1
            back(tmp + 1, i+1)
            arr[x][y] = 0
    return

N, M, H = map(int,input().split())
arr = [[0] * (N+1) for _ in range(H+1)]
data = []
for _ in range(M):
    a, b = map(int,input().split())
    arr[a][b] = 1

for i in range(1, H+1):
    for j in range(1, N):
        if not arr[i][j] and not arr[i][j+1] and not arr[i][j-1]:
            data.append([i,j])
result = 4
back(0,0)
print(result if result < 4 else -1)