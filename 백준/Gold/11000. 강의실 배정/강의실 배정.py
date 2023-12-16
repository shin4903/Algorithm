import sys
import heapq
N = int(sys.stdin.readline())
classtime = []
room = []
for _ in range(N):
    s, t = map(int,sys.stdin.readline().split())
    classtime.append([s,t])
classtime.sort()

for time in classtime:
    if not room:
        heapq.heappush(room,time[1])
    elif room:
        r = heapq.heappop(room)
        if r <= time[0]:
            heapq.heappush(room,time[1])
        elif r > time[0]:
            heapq.heappush(room,r)
            heapq.heappush(room, time[1])

print(len(room))