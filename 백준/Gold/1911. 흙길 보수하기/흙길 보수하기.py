N, L = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
arr.sort()
result = 0

now = arr[0][0]

for i in arr:
    if i[0] > now:
        now = i[0]
    dist = i[1] - now
    r = 1
    if dist % L == 0:
        r = 0
    cnt = dist // L + r
    now += cnt * L
    result += cnt
print(result)