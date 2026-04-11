# Heap

> A heap is a complete binary tree stored in an array. In a min heap, the parent node is always smaller than its children, which allows us to efficiently retrieve the minimum element in O(1) time and perform insert and remove operations in O(log n).

## 特徴

- 優先度管理
- Heapは配列で表現する

```
index:   0   1   2   3   4
value: [100, 80, 90, 70, 60]
```

### Complete Binary Tree

```
        100
       /   \
     80     90
    /  \
  70   60

左から順に詰めていく構造
```

### Heap Property（ヒープ条件）

```
Max Heap
親 ≥ 子
一番大きい値がトップ
```

```
Min Heap
親 ≤ 子
一番小さい値がトップ
```

## インデックス関係

| ノード | 計算式          |
| --- | ------------ |
| 親   | (i - 1) // 2 |
| 左の子 | 2i + 1       |
| 右の子 | 2i + 2       |


## 操作・計算量

1. Insert（末尾に追加) → 上に上げる（bubble up）
2. Remove（ルート削除) → 最後の要素を先頭 → 下に下げる（sink down）

| 操作     | 計算量      |
| ------ | -------- |
| insert | O(log n) |
| remove | O(log n) |
| peek   | O(1)     |

## 使い所

- Priority Queue
- Dijkstra’s Algorithm
- Top K problems

## Heap vs BST

|         | Heap   | BST      |
| ------- | ------ | -------- |
| 構造      | 完全二分木  | 任意       |
| 探索      | ❌（遅い）  | ◎（速い）    |
| 最大/最小取得 | ◎ O(1) | O(log n) |
