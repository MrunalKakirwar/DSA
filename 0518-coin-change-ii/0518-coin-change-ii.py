class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        d = [[-1] * (len(coins) + 1) for _ in range(amount + 1)]
        def helper(coins, amount, idx):
            # base case
            if (amount == 0):
                return 1
            if (amount < 0 or idx == len(coins)):
                return 0
            if d[amount][idx] != -1:
                return  d[amount][idx]

            # logic
            d[amount][idx] = helper(coins, amount - coins[idx] , idx)
           
            d[amount][idx] += helper(coins, amount, idx + 1)
            return d[amount][idx]

        return helper(coins, amount, 0)