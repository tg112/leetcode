# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Example 2:
# Input: nums = [0,1,1]

# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]

# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints:
# 3 <= nums.length <= 1000
# -10^5 <= nums[i] <= 10^5

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. 配列を昇順にソート（2ポインタ法と重複排除の前提条件）
        nums.sort()
        result = []
        n = len(nums)

        # 基準値 `nums[i]` を固定するためのループ
        for i in range(n - 2):
            # 【最適化】配列はソート済みのため、最小値である nums[i] が 0 を超えた時点で
            # その後どのように3つの数を足しても合計が 0 になることは絶対にない
            if nums[i] > 0:
                break

            # 【重複排除①】1つ前の要素と同じ値ならスキップ（同じ組み合わせの生成を防ぐ）
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 2. 残りの範囲を2ポインタ（左右両端から挟み撃ち）で探索
            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # 解が見つかったので結果に追加
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # 【重複排除②】leftポインタの次が同じ値ならスキップ
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 【重複排除③】rightポインタの手前が同じ値ならスキップ
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    # 合計が 0 より小さい場合、値を大きくしたいので左ポインタを右へ
                    left += 1
                else:
                    # 合計が 0 より大きい場合、値を小さくしたいので右ポインタを左へ
                    right -= 1
        return result