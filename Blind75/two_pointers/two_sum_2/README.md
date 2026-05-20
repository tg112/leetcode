# Two Sum II - Input Array Is Sorted

## 問題概要
昇順ソート済みの整数配列 `numbers`（1-indexed）が与えられる。合計が `target` となる2つの数のインデックスを `[index1, index2]`（1-indexed）で返す。  
解は必ず1つ存在し、同じ要素を2回使ってはいけない。追加のメモリは O(1) しか使えない。

## 計算量
- 時間計算量: O(n)
- 空間計算量: O(1)

## アプローチ

**Two Pointers** — ソート済み配列だからこそ使える手法。

1. `left = 0`、`right = len(numbers) - 1` に初期化
2. `current_sum = numbers[left] + numbers[right]` を計算:
   - `== target` → `[left+1, right+1]` を返す（1-indexed に変換）
   - `< target` → 合計を増やしたいので `left` を右へ
   - `> target` → 合計を減らしたいので `right` を左へ

## ポイント

**Two Sum 1 との違い**  
Two Sum 1 はソートされていないためハッシュマップで O(n) 空間を使う。  
Two Sum 2 はソート済みなので Two Pointers が使え、O(1) の追加空間で解ける。

**ポインタを内側に動かすだけで全組み合わせをカバーできる理由**  
ソート済みなので `left` を右に動かせば合計が増え、`right` を左に動かせば合計が減ることが保証されている。
