# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 文字とその文字が「最後に登場したインデックス」を記録する辞書
        char_index_map = {}
        max_length = 0
        left = 0  # 窓の左端

        # 右端（right）を1つずつ進めていく
        for right in range(len(s)):
            current_char = s[right]

            # もし新しく入ってきた文字が過去に登場しており、
            # かつその位置が「現在の窓の内側（left以上）」にある場合
            if current_char in char_index_map and char_index_map[current_char] >= left:
                # 重複を避けるため、左端を「過去の登場位置の1つ右」まで一気にワープさせる
                left = char_index_map[current_char] + 1

            # 文字の最新の登場位置をアップデート（または新規登録）
            char_index_map[current_char] = right
            
            # 現在の有効な窓の長さ（right - left + 1）で最大値を更新
            max_length = max(max_length, right - left + 1)

        return max_length
