class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers (keep track of the profit u make)
        left = 0 # left is buy
        right = 0 # right is sell
        bestProfit = 0 # keep track of best profit

        while right < len(prices): # until out of bounds
            profit = prices[right] - prices[left]
            # determine when to move either pointer
            if prices[left] > prices[right]:
                left += 1 # get off that pricy day
            else:
                # should be greater than or equal to 0 (earned profit)
                bestProfit = max(profit, bestProfit) 
                right += 1

        return bestProfit