import sys
import heapq

N = int(sys.stdin.readline())
plus = []
minus = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(plus,x)
    elif x < 0:
        heapq.heappush(minus,-x)
    elif x == 0:
        if not minus and plus:
            print(heapq.heappop(plus))
        elif not plus and minus:
            print(-heapq.heappop(minus))
        elif not plus and not minus:
            print(0)
        elif plus and minus:
            p = heapq.heappop(plus)
            m = heapq.heappop(minus)
            if abs(p) >= abs(m):
                print(-m)
                heapq.heappush(plus,p)
            elif abs(p) < abs(m):
                print(p)
                heapq.heappush(minus,m)
