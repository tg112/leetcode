class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        itr1, itr2 = 0, 0
        while itr1 < len(s) and itr2 < len(t):
            if s[itr1] == t[itr2]:
                itr1 += 1
                itr2 += 1
            else:
                itr2 += 1

        return itr1 == len(s)

    def refactored_isSubSequence(self, s: str, t: str) -> bool:
        i = 0
        # sが空文字の場合、即座にTrueを返すためのガード
        if not s:
            return True
        
        for char in t:
            if i < len(s) and char == s[i]:
                i += 1
        
        return i == len(s)

    def another_solution(self, s: str, t: str) -> bool:
        it = iter(t)
        # sの各文字が it の中に順番に存在するかを確認
        return all(char in it for char in s)

