class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0

        while buy < len(prices):
            sell = buy

            while sell < len(prices) - 1:
                sell += 1
                curr_profit = prices[sell] - prices[buy]
                max_profit = max(curr_profit, max_profit)

            buy += 1

        return max_profit