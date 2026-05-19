#You are given an integer array heights where heights[i] represents the height of the i th bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 1. 左右の両端にポインタを配置
        left = 0
        right = len(heights) - 1
        max_area = 0

        # 左右のポインタが交差するまでループ
        while left < right:
            # 2. 現在のコンテナの面積を計算
            # 高さは「低い方の壁」に制限され、幅は「右ポインタ - 左ポインタ」
            current_height = min(heights[left], heights[right])
            current_width = right - left
            area = current_height * current_width

            # 3. 最大面積の更新
            max_area = max(max_area, area)

            # 4. ポインタの移動（貪欲法）
            # 横幅が狭まる以上、面積が大きくなる可能性を残すために
            # ボトルネックとなっている「低い方の壁」のポインタを内側に進める
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area