class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #Left = Buy | Right = Sell

        maxP = 0

        while r < len(prices):
            #Measure Profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
        