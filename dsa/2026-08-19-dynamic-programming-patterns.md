# Dynamic Programming - Patterns

> _2026-08-19_ | Category: **dsa**

Break problems into overlapping subproblems.

```java
// 1. Fibonacci (Bottom-up, O(n) time, O(1) space)
public int fib(int n) {
    int prev2 = 0, prev1 = 1;
    for (int i = 2; i <= n; i++) {
        int curr = prev1 + prev2;
        prev2 = prev1; prev1 = curr;
    }
    return prev1;
}

// 2. Coin Change (minimum coins to make amount)
public int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, amount + 1);
    dp[0] = 0;
    for (int i = 1; i <= amount; i++)
        for (int c : coins)
            if (c <= i) dp[i] = Math.min(dp[i], dp[i - c] + 1);
    return dp[amount] > amount ? -1 : dp[amount];
}
```

**DP Steps**: 1. Define state → 2. Recurrence relation → 3. Base case → 4. Optimize space.
