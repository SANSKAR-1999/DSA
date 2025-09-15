class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price - min_price > max_profit:
                max_profit = price - min_price
            if price < min_price:
                min_price = price
        return max_profit
        