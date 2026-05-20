# Maximum Subarray (Kadane's Algorithm)

## 問題概要
整数配列 `nums` から、要素の合計が最大となる連続部分配列を見つけ、その合計値を返す。

## 計算量
- 時間計算量: O(n)
- 空間計算量: O(1)

## アプローチ

**Kadane's Algorithm** — 「今ここから再スタートする」か「前の合計に乗り続ける」かを毎ステップ選択する。

```
current_sum = max(num, current_sum + num)
```

- `current_sum + num < num`（＝`current_sum < 0`）なら、前の累積は足を引っ張るだけなので捨てて `num` から再スタート
- そうでなければ、前の累積を活かして伸ばし続ける

毎ステップで `max_sum = max(max_sum, current_sum)` を更新し、最終的な最大値を記録する。

## ポイント
- 初期値を `nums[0]` にする理由：配列がすべて負の場合でも正しく最大値を返すため（`0` や `-∞` で初期化すると全負配列で誤答になる）
- `max(num, current_sum + num)` は「負の累積を切り捨てる」操作と等価で、`current_sum` が負になった瞬間にリセットされる
