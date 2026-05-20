# Given two strings s and t, return the shortest substring of s such that every character in t, 
# including duplicates, is present in the substring. 
# If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

# Example 1:
# Input: s = "OUZODYXAZV", t = "XYZ"
# Output: "YXAZ"
# Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

# Example 2:
# Input: s = "xyz", t = "xyz"
# Output: "xyz"

# Example 3:
# Input: s = "x", t = "xy"
# Output: ""

from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # エッジケース：どちらかが空文字なら、満たせる条件はないので空を返す
        if not s or not t:
            return ""

        # 1. ターゲット文字列 't' の文字カウントマップを作成
        dict_t = Counter(t)
        # 必要な「ユニークな文字の種類数」を取得（例: "AABC" なら 'A','B','C' の 3種類）
        required = len(dict_t)
        
        # ポインタと窓内の状態管理変数
        left, right = 0, 0
        formed = 0  # 現在の窓の中で、tの条件（文字数）を満たしたユニークな文字の種類数
        window_counts = defaultdict(int)  # 現在の窓内にある各文字のカウント
        
        # 最小ウィンドウの情報を記録する変数 (長さ, 左端インデックス, 右端インデックス)
        min_len = float("inf")
        min_left, min_right = 0, 0

        # 右端ポインタ（right）を1文字ずつ進めていく
        while right < len(s):
            char = s[right]
            window_counts[char] += 1

            # 新しく入った文字によって、tの要求する「その文字の必要数」を満たした瞬間
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            
            # 【縮小フェーズ】tに含まれるすべての文字が揃っている間、左端（left）を縮めて最小を探る
            while left <= right and formed == required:
                char = s[left]

                # 現在の窓の長さが、これまでの最小記録を更新したらインデックスを保存
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left, min_right = left, right

                # 左端の文字を窓から追い出す
                window_counts[char] -= 1
                
                # 追い出した結果、tが要求する数を下回ってしまった瞬間、条件不達成（formedを減らす）
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                
                # 左端を次に進める
                left += 1
            
            # 右端を次に進める
            right += 1
        
        # 一度も条件を満たせなかった場合は空文字、満たせた場合は記録したインデックスで1度だけ切り出す
        return "" if min_len == float("inf") else s[min_left:min_right + 1]
