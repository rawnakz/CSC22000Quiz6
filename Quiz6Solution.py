def coinChange(coins, amount):
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    
    coins = [1, 2, 5]
    amount = 11
    print("Coins:", coins)
    print("Amount:", amount)
    print("Fewest coins needed:", coinChange(coins, amount))  # This should be three
