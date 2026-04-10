# BinarySearchTree

> A Binary Search Tree is a binary tree where each node has at most two children, and for every node, values in the left subtree are smaller and values in the right subtree are larger.
> This allows search, insertion, and deletion to be performed in O(log n) on average.
> In the worst case, the time complexity becomes O(n) when the tree is unbalanced.

## Rule
`左の子 < 親 < 右の子`

```text
        10
       /  \
      8    12
     / \     \
    5   9     15
```

## 計算量

Worst Case: `Because the tree can become skewed like a linked list when values are inserted in sorted order.`

ex) `1 → 2 → 3 → 4 → 5`

```text
Linked Listと同じ構造
1
 \
  2
   \
    3
     \
      4
```

| 操作     | 平均       | 最悪   |
| ------ | -------- | ---- |
| search | O(log n) | O(n) |
| insert | O(log n) | O(n) |
| delete | O(log n) | O(n) |

| 観点       | BST          | Linked List |
| -------- | ------------ | ----------- |
| 構造       | 木（Tree）      | 線（Linear）   |
| 探索       | O(log n)（平均） | O(n)        |
| 挿入       | O(log n)     | O(1)（先頭なら）  |
| 順序       | ソート状態を維持     | 順序なし        |
| ランダムアクセス | 不可           | 不可          |




A Binary Search Tree is a tree data structure where each node follows the rule that values in the left subtree are smaller and values in the right subtree are larger. This allows search operations to run in O(log n) on average, unlike a linked list which requires O(n) time because it must traverse nodes sequentially. However, if the tree becomes unbalanced, the time complexity degrades to O(n), making it similar to a linked list.

