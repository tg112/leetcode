# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Example 1:
# Input: prices = [10,1,5,6,7,1]
# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

# Example 2:
# Input: prices = [10,8,7,5,2]
# Output: 0
# Explanation: No profitable transactions can be made, thus the max profit is 0.

# Constraints:
# 1 <= prices.length <= 100
# 0 <= prices[i] <= 100

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # 配列が空、または1日分しかない場合は取引できないので利益は0
        if not prices:
            return max_profit

        # 最初の日の価格を「暫定の最安値」としてスタート
        min_price = prices[0]
        
        # 2日目以降の価格を順番にチェック
        for price in prices[1:]:
            # 1. これまでの最安値（過去の購入候補）を更新
            min_price = min(price, min_price)

            # 2. 「今日の価格 - これまでの最安値」で、今日売った場合の利益を計算し、最大利益を更新
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
