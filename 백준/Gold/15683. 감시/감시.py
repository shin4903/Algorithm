import copy
def back(arr, idx, tmp):
    global result
    if idx > len(data) - 1:
        result = max(result, tmp)
        return
    x, y = data[idx][0], data[idx][1]
    if arr[x][y] == 1:
        cnt = 0
        arr2 = copy.deepcopy(arr)
        for i in range(x - 1, -1, -1):
            if arr2[i][y] == 6:
                break
            elif arr2[i][y] == 0:
                arr2[i][y] = '#'
                cnt += 1
        back(arr2, idx+1, tmp + cnt)

        cnt = 0
        arr2 = copy.deepcopy(arr)
        for i in range(x + 1, N):
            if arr2[i][y] == 6:
                break
            elif arr2[i][y] == 0:
                arr2[i][y] = '#'
                cnt += 1
        back(arr2, idx+1, tmp + cnt)

        cnt = 0
        arr2 = copy.deepcopy(arr)
        for j in range(y - 1, -1, -1):
            if arr2[x][j] == 6:
                break
            elif arr2[x][j] == 0:
                arr2[x][j] = '#'
                cnt += 1
        back(arr2, idx + 1, tmp + cnt)

        cnt = 0
        arr2 = copy.deepcopy(arr)
        for j in range(y + 1, M):
            if arr2[x][j] == 6:
                break
            elif arr2[x][j] == 0:
                arr2[x][j] = '#'
                cnt += 1
        back(arr2, idx + 1, tmp + cnt)

    elif arr[x][y] == 2:
        cnt = 0
        arr2 = copy.deepcopy(arr)
        for i in range(x - 1, -1, -1):
            if arr2[i][y] == 6:
                break
            elif arr2[i][y] == 0:
                arr2[i][y] = '#'
                cnt += 1
        for i in range(x + 1, N):
            if arr2[i][y] == 6:
                break
            elif arr2[i][y] == 0:
                arr2[i][y] = '#'
                cnt += 1
        back(arr2, idx + 1, tmp + cnt)

        cnt = 0
        arr2 = copy.deepcopy(arr)
        for j in range(y - 1, -1, -1):
            if arr2[x][j] == 6:
                break
            elif arr2[x][j] == 0:
                arr2[x][j] = '#'
                cnt += 1
        for j in range(y + 1, M):
            if arr2[x][j] == 6:
                break
            elif arr2[x][j] == 0:
                arr2[x][j] = '#'
                cnt += 1
        back(arr2, idx + 1, tmp + cnt)

    elif arr[x][y] == 3:
        cnt = 0
        arr2 = copy.deepcopy(arr)
        for i in range(x - 1, -1, -1):
            if arr2[i][y] == 6:
                break
            elif arr2[i][y] == 0:
                arr2[i][y] = '#'
                cnt += 1
        for j in range(y + 1, M):
            if arr2[x][j] == 6:
                break
            elif arr2[x][j] == 0:
                arr2[x][j] = '#'
                cnt += 1
        back(arr2, idx + 1, tmp + cnt)

        cnt = 0
        arr2 = copy.deepcopy(arr)
        for i in range(x + 1, N):
            if arr2[i][y] == 6:
                break
            elif arr2[i][y] == 0:
                arr2[i][y] = '#'
                cnt += 1
        for j in range(y + 1, M):
            if arr2[x][j] == 6:
                break
            elif arr2[x][j] == 0:
                arr2[x][j] = '#'
                cnt += 1
        back(arr2, idx + 1, tmp + cnt)

        cnt = 0
        arr2 = copy.deepcopy(arr)
        for i in range(x + 1, N):
            if arr2[i][y] == 6:
                break
            elif arr2[i][y] == 0:
                arr2[i][y] = '#'
                cnt += 1
        for j in range(y - 1, -1, -1):
            if arr2[x][j] == 6:
                break
            elif arr2[x][j] == 0:
                arr2[x][j] = '#'
                cnt += 1
        back(arr2, idx + 1, tmp + cnt)

        cnt = 0
        arr2 = copy.deepcopy(arr)
        for i in range(x - 1, -1, -1):
            if arr2[i][y] == 6:
                break
            elif arr2[i][y] == 0:
                arr2[i][y] = '#'
                cnt += 1
        for j in range(y - 1, -1, -1):
            if arr2[x][j] == 6:
                break
            elif arr2[x][j] == 0:
                arr2[x][j] = '#'
                cnt += 1
        back(arr2, idx + 1, tmp + cnt)

    elif arr[x][y] == 4:
        cnt = 0
        arr2 = copy.deepcopy(arr)
        for i in range(x - 1, -1, -1):
            if arr2[i][y] == 6:
                break
            elif arr2[i][y] == 0:
                arr2[i][y] = '#'
                cnt += 1
        for i in range(x + 1, N):
            if arr2[i][y] == 6:
                break
            elif arr2[i][y] == 0:
                arr2[i][y] = '#'
                cnt += 1
        for j in range(y - 1, -1, -1):
            if arr2[x][j] == 6:
                break
            elif arr2[x][j] == 0:
                arr2[x][j] = '#'
                cnt += 1
        back(arr2, idx + 1, tmp + cnt)

        cnt = 0
        arr2 = copy.deepcopy(arr)
        for i in range(x - 1, -1, -1):
            if arr2[i][y] == 6:
                break
            elif arr2[i][y] == 0:
                arr2[i][y] = '#'
                cnt += 1
        for i in range(x + 1, N):
            if arr2[i][y] == 6:
                break
            elif arr2[i][y] == 0:
                arr2[i][y] = '#'
                cnt += 1
        for j in range(y + 1, M):
            if arr2[x][j] == 6:
                break
            elif arr2[x][j] == 0:
                arr2[x][j] = '#'
                cnt += 1
        back(arr2, idx + 1, tmp + cnt)

        cnt = 0
        arr2 = copy.deepcopy(arr)
        for i in range(x - 1, -1, -1):
            if arr2[i][y] == 6:
                break
            elif arr2[i][y] == 0:
                arr2[i][y] = '#'
                cnt += 1
        for j in range(y - 1, -1, -1):
            if arr2[x][j] == 6:
                break
            elif arr2[x][j] == 0:
                arr2[x][j] = '#'
                cnt += 1
        for j in range(y + 1, M):
            if arr2[x][j] == 6:
                break
            elif arr2[x][j] == 0:
                arr2[x][j] = '#'
                cnt += 1
        back(arr2, idx + 1, tmp + cnt)

        cnt = 0
        arr2 = copy.deepcopy(arr)
        for i in range(x + 1, N):
            if arr2[i][y] == 6:
                break
            elif arr2[i][y] == 0:
                arr2[i][y] = '#'
                cnt += 1
        for j in range(y - 1, -1, -1):
            if arr2[x][j] == 6:
                break
            elif arr2[x][j] == 0:
                arr2[x][j] = '#'
                cnt += 1
        for j in range(y + 1, M):
            if arr2[x][j] == 6:
                break
            elif arr2[x][j] == 0:
                arr2[x][j] = '#'
                cnt += 1
        back(arr2, idx + 1, tmp + cnt)

    elif arr[x][y] == 5:
        cnt = 0
        arr2 = copy.deepcopy(arr)
        for i in range(x - 1, -1, -1):
            if arr2[i][y] == 6:
                break
            elif arr2[i][y] == 0:
                arr2[i][y] = '#'
                cnt += 1
        for i in range(x + 1, N):
            if arr2[i][y] == 6:
                break
            elif arr2[i][y] == 0:
                arr2[i][y] = '#'
                cnt += 1
        for j in range(y - 1, -1, -1):
            if arr2[x][j] == 6:
                break
            elif arr2[x][j] == 0:
                arr2[x][j] = '#'
                cnt += 1
        for j in range(y + 1, M):
            if arr2[x][j] == 6:
                break
            elif arr2[x][j] == 0:
                arr2[x][j] = '#'
                cnt += 1
        back(arr2, idx + 1, tmp + cnt)

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
data = []
wall = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != 6:
            data.append([i,j])
        if arr[i][j] == 6:
            wall += 1

result = 0
back(arr, 0, 0)
print(N*M - len(data) - result - wall)