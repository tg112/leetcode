# Dynamic Programming（DP）まとめ

## What is Dynamic Programming?

> Dynamic Programming is a technique for solving problems by breaking them into smaller subproblems and storing the results to avoid redundant computations.

---

## Core Concepts（最重要）

### ① Overlapping Subproblems

> 同じ部分問題が何度も繰り返し出てくること

#### 例：フィボナッチ

```
fib(5)
→ fib(4) + fib(3)
→ fib(3) が何回も出てくる
```

`無駄な計算が発生する`

---

### ② Optimal Substructure（最適部分構造）

> 問題の最適解が「部分問題の最適解」から構成できること

#### 例：フィボナッチ

```
fib(n) = fib(n-1) + fib(n-2)
```

`小さい問題の答えを使って全体を解く`

---

## DPの2つのアプローチ

### ① Top-down（Memoization）

* 再帰で解く
* 計算結果を保存（cache）

```python
memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```

---

### ② Bottom-up（Tabulation）

* 小さい問題から順に解く
* ループで積み上げる

```python
def fib(n):
    if n == 0:
        return 0
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]
```

---

## Complexity

| 方法    | 時間     | 空間   |
| ----- | ------ | ---- |
| 普通の再帰 | O(2^n) | O(n) |
| DP    | O(n)   | O(n) |
| 最適化   | O(n)   | O(1) |

---

## なぜDPが必要？

### ❌ 普通の再帰

* 同じ計算を何度もする
* 非効率

### ✅ DP

* 一度計算したら再利用
* 効率化（高速化）

---

## DPを見抜くヒント

以下があればDPを疑う

* 同じ計算が繰り返されている（Overlapping Subproblems）
* 小さい問題で解ける（Optimal Substructure）
* 最大/最小/組み合わせを求める問題

---

## よくある問題パターン

* Fibonacci
* Climbing Stairs
* House Robber
* Knapsack Problem
* Longest Increasing Subsequence

---

## Interview Answer

> Dynamic programming is an optimization technique used when a problem has overlapping subproblems and optimal substructure. It improves efficiency by storing results of subproblems and reusing them instead of recomputing.

---

## One-line Summary

> 「DP = 同じ計算を避けて、最適解を積み上げる」

---

# Memoizationとは？

> Memoization is a technique where we store the results of expensive function calls and reuse them when the same inputs occur again.

一言でいうと `「一度計算した結果を覚えておく」`

## Memoizationの流れ

```
1. 関数を呼ぶ
2. すでに計算済み？ → YES → return
3. 未計算 → 計算する
4. 結果を保存
5. return
```

## どんなとき使う？

以下が揃うと使う

- 同じ計算が繰り返される
- 再帰で書ける
- 最適解問題
