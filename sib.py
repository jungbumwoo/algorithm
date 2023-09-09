def count_stair_numbers(N):
    MOD = 10**9
    dp = [[[0] * 1024 for _ in range(10)] for _ in range(N + 1)]

    for i in range(1, 10):
        dp[1][i][1 << i] = 1

    for n in range(2, N + 1):
        for i in range(10):
            for j in range(1024):
                if i > 0:
                    dp[n][i][j | (1 << i)] += dp[n - 1][i - 1][j]
                if i < 9:
                    dp[n][i][j | (1 << i)] += dp[n - 1][i + 1][j]
                dp[n][i][j | (1 << i)] %= MOD

    ans = sum(dp[N][i][1023] for i in range(10))
    print(dp)
    return ans % MOD

N = 10
result = count_stair_numbers(N)
print(result)