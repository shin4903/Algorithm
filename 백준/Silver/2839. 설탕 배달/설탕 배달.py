N = int(input())
bags = [3, 5]
dp = [-1] * 5001
for bag in bags:
    dp[bag] = 1
    for i in range(bag+1,N+1):
        if dp[i-bag] > -1:
            if dp[i] > 0:
                dp[i] = min(dp[i - bag] + 1, dp[i])
            elif dp[i] == -1:
                dp[i] = dp[i - bag] + 1
print(dp[N])