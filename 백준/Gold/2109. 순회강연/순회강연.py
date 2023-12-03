import heapq
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[1],-x[0]))
tmp = []

for i in arr:
    heapq.heappush(tmp, i[0])
    if len(tmp) > i[1]:
        heapq.heappop(tmp)
print(sum(tmp))