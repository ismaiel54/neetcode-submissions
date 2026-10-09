class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {0:0}

        def min_coin(amt):
            if amt in memo:
                return memo[amt]
            
            minn = float('inf')
            for c in coins:
                diff = amt - c
                if diff < 0:
                    break
                minn = min(minn, 1 + min_coin(diff))
            
            memo[amt] = minn
            return minn
        
        result = min_coin(amount)
        if result < float('inf'):
            return result
        else:
            return -1


        
            


        