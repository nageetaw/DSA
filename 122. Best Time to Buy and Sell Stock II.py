class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # This statemnet means "At most one share at any time" means you can buy one share, sell it whenever you want (even the same day), but you have to sell that share before you are allowed to buy another one.
        # "You can only hold at most one share of the stock at any time." 
        
        # Space Complexity = O(1)
        max_profit =0
        buy_day , sell_day = 0,1

        # Time Complexity = O(n)
        while sell_day < len(prices):
            
            profit = prices[sell_day] - prices[buy_day]

            if profit < 0:
                buy_day = sell_day
            
            else:
                max_profit = profit + max_profit
                buy_day +=1

            sell_day +=1
        
        return max_profit

            


        