import sys
import heapq
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if not arr:
            print(0)
        elif arr:
            print(-heapq.heappop(arr))
    elif x:
        heapq.heappush(arr,-x)