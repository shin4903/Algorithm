import sys
input = sys.stdin.readline
N = int(input())
T = [0]
P = [0]
dp = [0] * (N+1)
for _ in range(N):
    t, p = map(int,input().split())
    T.append(t)
    P.append(p)

for i in range(1,N+1):
    dp[i] = max(dp[i], dp[i - 1])
    date = i + T[i] - 1
    if date <= N:
        dp[date] = max(dp[date],dp[i - 1] + P[i])
print(max(dp))