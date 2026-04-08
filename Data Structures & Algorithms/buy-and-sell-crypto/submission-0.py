class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        global_profit = 0
        local_profit = 0
        for i in range(len(prices)):
            local_profit=0
            for j in range(i,len(prices)):
                profit = prices[j]-prices[i] 
                if profit > local_profit:
                    local_profit = profit
            if global_profit < local_profit:
                global_profit = local_profit
    
        return global_profit