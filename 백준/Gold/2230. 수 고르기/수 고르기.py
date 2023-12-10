def TP(a, n, key):
    global result
    start = 0
    end = 0
    while start <= end and end < n:
        if a[end] - a[start] >= key:
            result = min(result, a[end] - a[start])
            start += 1
        elif a[end] - a[start] < key:
            end += 1
    return


N, M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
result = int(2e9)
TP(arr, N, M)
print(result)