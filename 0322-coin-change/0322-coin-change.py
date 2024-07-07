class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        d = [[-1] * (len(coins)+1) for _ in range(amount + 1)]

        def helper(coins, amount, idx):

            # base 
            if(amount == 0):
                return 0
            if(amount < 0 or len(coins) == idx):
                return 99999
        
            if d[amount][idx] != -1:
                return d[amount][idx]
        
            # logic
            choose = 1 + helper (coins, amount - coins[idx], idx)
            notChoose = helper (coins, amount, idx + 1)
            d[amount][idx] = min (choose, notChoose)
            return d[amount][idx]

        rtype = helper (coins, amount, 0)

        if rtype >= 99999:
            return -1
        return rtype