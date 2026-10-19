class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        
        left = 0
        right = 1

        while right < len(prices):
            buy = prices[left]
            sell = prices[right]
            if sell > buy:
                profits.append(sell-buy)
                right += 1
            elif sell == buy:
                right += 1
            else:
                left = right
                right += 1

        if len(profits) == 0:
            return 0
        return max(profits)