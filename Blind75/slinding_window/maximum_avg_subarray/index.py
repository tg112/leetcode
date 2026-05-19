# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and 
# return this value. Any answer with a calculation error less than 10-5 will be accepted.

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = 0
        # 0からkまでの最初の合計を計算する
        for i in range(k):
            current_sum += nums[i]

        max_sum = current_sum

        start_index = 0
        end_index = k


        while end_index < len(nums):
            # 前回の最初のindexの値をcurren_numから引く
            current_sum -= nums[start_index]
            start_index += 1

            # 前回のend_indexの次のindexの値を追加する
            current_sum += nums[end_index]
            end_index += 1

            max_sum = max(max_sum, current_sum)
        
        return max_sum / k

    def more_efficient_solution(self, nums: List[int], k: int) -> float:
        # 1. 最初の窓（インデックス 0 から k-1 まで）の合計を計算
        current_sum = sum(nums[:k])
        max_sum = current_sum

        # 2. 窓を1つずつ右にスライドさせる
        # i は「新しく窓に入る要素（右端）」のインデックス
        for i in range(k, len(nums)):
            # [新しく入る要素] を足して、[左端から外れる要素 (i - k)] を引く
            current_sum += nums[i] - nums[i - k]

            # 最大合計値の更新
            if current_sum > max_sum:
                max_sum = current_sum
        
        # 3. 合計の最大値を最後に k で割って平均値を返す
        return max_sum / k

