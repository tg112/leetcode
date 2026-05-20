# Product of Array Except Self

## 問題概要
整数配列 `nums` が与えられる。`answer[i]` が `nums[i]` 以外のすべての要素の積となる配列 `answer` を返す。  
**除算は使用禁止**。O(n) で解くこと。

## 計算量

**解法1（left / right 配列）**
- 時間計算量: O(n)
- 空間計算量: O(n) — left・right の2つの配列

**解法2（prefix / postfix、空間最適化）**
- 時間計算量: O(n)
- 空間計算量: O(1) — 出力配列を除く

## アプローチ

`nums[i]` を除く積 ＝ **左側全部の積** × **右側全部の積**

**解法1：left / right 配列**

```
left[i]  = nums[0] * ... * nums[i-1]  （i より左の積）
right[i] = nums[i+1] * ... * nums[n-1] （i より右の積）
result[i] = left[i] * right[i]
```

**解法2：prefix / postfix（空間最適化）**

1. 左から `prefix` 積を `result` に直接書き込む
2. 右から `postfix` 積を掛け合わせて上書きする

## ポイント
- `left[0] = 1`、`right[n-1] = 1` と初期化するのは「左端の左側」「右端の右側」には要素がないため（積の単位元は1）
- 解法1の `right` の逆順ループ：`range(len(nums) - 2, -1, -1)` は `n-2 → 0` を表す（`range(start, stop_exclusive, step)`）
- `zip` と list comprehension で `result = [l * r for l, r in zip(left, right)]` と簡潔に書ける
