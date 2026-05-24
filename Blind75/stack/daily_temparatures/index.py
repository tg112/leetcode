from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = n * [0]  # 結果を格納する配列（あらかじめ0で初期化）
        stack = []         # 未来の「高い気温のインデックス」を保持する単調スタック

        # 未来（末尾）から過去（先頭）に向かって逆順に走査する
        for i in range(n - 1, -1, -1):

            # 現在の気温（temperatures[i]）以上の気温がスタックのトップにある間、
            # それより低い（または同じ）未来の気温は「今日から見て最初の暖かい日」になり得ないので、
            # 容赦なくスタックから排除（pop）する
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            
            # whileループを抜けた後にスタックに要素が残っていれば、
            # そのスタックのトップ（stack[-1]）こそが「今日以降で、今日より暖かい最初の日」のインデックス
            if stack:
                results[i] = stack[-1] - i  # 暖かい日までの日数を計算して格納
            
            # 今日のインデックスをスタックに積んで、過去の日のための「未来の候補」にする
            stack.append(i)

        return results