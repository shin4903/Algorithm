N, K = map(int,input().split())
data = [int(input()) for _ in range(N)]
data.sort()
dp = [-1] * (K+1)
dp[0] = 0
for coin in data:
    if coin <= K:
        dp[coin] = 1
        for i in range(coin,K+1):
            if dp[i-coin] > 0:
                if dp[i] != -1:
                    dp[i] = min(dp[i],dp[i - coin] + 1)
                else:
                    dp[i] = dp[i - coin] + 1
print(dp[K])