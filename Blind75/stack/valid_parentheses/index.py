# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
# The input string s is valid if and only if:
#   1. Every open bracket is closed by the same type of close bracket.
#   2. Open brackets are closed in the correct order.
#   3. Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Example 1:
# Input: s = "[]"
# Output: true

# Example 2:
# Input: s = "([{}])"
# Output: true

# Example 3:
# Input: s = "[(])"
# Output: false
# Explanation: The brackets are not closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        # 開き括弧を一時的に保存するためのスタック
        stack = []

        # 閉じ括弧をキー、対応する開き括弧を値としたハッシュマップ
        # これにより、閉じ括弧が来たときに「何がセットされるべきか」を一発で引ける
        bracket_map = {")": "(", "]": "[", "}": "{"}

        for char in s:
            # 1. 現在の文字が「閉じ括弧」の場合
            if char in bracket_map:
                # スタックが空でなく、かつスタックの一番上（最後に開いた括弧）が
                # 現在の閉じ括弧と正しくペアになる場合
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()  # ペアが成立したのでスタックから取り除く
                else:
                    return False # ペアが合わない、または対応する開き括弧がない場合は即座に無効
            
            # 2. 現在の文字が「開き括弧」の場合
            else:
                stack.append(char)  # 次に閉じ括弧が来るまでスタックにキープしておく
        
        # すべての文字を処理した後、スタックが完全に空であればすべての括弧が正しく閉じられた証拠 (True)
        # スタックに開き括弧が残ってしまっていれば不完全 (False)
        return not stack
