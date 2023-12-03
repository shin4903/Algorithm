import heapq

N, K = map(int,input().split())

gems = [list(map(int,input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
gems.sort()
bags.sort()
result = 0
tmp = []

for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(tmp, -gems[0][1])
        heapq.heappop(gems)
    if tmp:
        result -= heapq.heappop(tmp)
print(result)