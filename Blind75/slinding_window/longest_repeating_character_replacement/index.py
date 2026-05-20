# You are given a string s consisting of only uppercase english characters and an integer k. 
# You can choose up to k characters of the string and replace them with any other uppercase English character.
# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # 窓の中にある各文字の登場回数を記録する辞書
        max_len = 0  # 最終的に返す「条件を満たす最長の窓の長さ」
        max_frequency = 0  # 窓の中で「最も多く登場する文字」のカウント数
        left = 0  # 窓の左端ポインタ

        # 右端ポインタ（right）を1つずつ進めていく
        for right in range(len(s)):
            # 1. 新しく窓に入ってきた文字をカウント
            current_char = s[right]
            count[current_char] = count.get(current_char, 0) + 1

            # 2. 窓内の「単一文字の最大登場数」の最高記録を更新
            max_frequency = max(max_frequency, count[current_char])

            # 3. 「窓の長さ - 最多文字の数」が k を超えているか判定
            # 超えている場合、k個の書き換えだけでは文字を統一できないので、
            # 条件を満たすまで左端（left）を削って窓を小さくする
            while (right - left + 1) - max_frequency > k:
                count[s[left]] -= 1  # 左端から外れる文字のカウントを減らす
                left += 1  # 左端を右に進める

            # 4. whileを抜けた時点の窓は「条件を満たす有効な窓」なので、最大長さを更新
            current_window_len = right - left + 1
            max_len = max(max_len, current_window_len)
        
        return max_len
