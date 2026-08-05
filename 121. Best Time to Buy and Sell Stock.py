class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit =0
        n = len(prices)
        
        # Space Complexity: O(n)
        buy_day , sell_day = 0,1

        # Time Complexity O(n) 
        while sell_day < n:
            profit = prices[sell_day] - prices[buy_day]

            if profit <=0:
                # buy on the day when profit is negative, because stocks are very low priced
                buy_day = sell_day 
            else:
                max_profit = max(profit, max_profit)
            
            sell_day +=1
        
        return max_profit

        