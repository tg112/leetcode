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


## Recursion vs Iteration

### 🔁 Overview

|             | Recursion                | Iteration              |
| ----------- | ------------------------ | ---------------------- |
| Definition  | Function calls itself    | Uses loops (while/for) |
| Structure   | Uses call stack          | Uses variables         |
| Readability | More intuitive for trees | More explicit          |

---

### ✅ Advantages

#### Recursion

* Cleaner and shorter code
* Natural for tree/graph problems
* Easier to reason about divide & conquer

#### Iteration

* More memory efficient
* No risk of stack overflow
* Faster in practice

---

### ❌ Disadvantages

#### Recursion

* Uses call stack → extra memory
* Risk of stack overflow (deep recursion)
* Slightly slower

#### Iteration

* Code can be more complex
* Harder to implement for recursive structures

---

### ⏱ Time & Space

|                  | Recursion         | Iteration |
| ---------------- | ----------------- | --------- |
| Time Complexity  | Same              | Same      |
| Space Complexity | O(h) (call stack) | O(1)      |

※ h = tree height

---

### 🎯 When to Use

#### Use Recursion when:

* Tree / Graph DFS
* Divide & Conquer (MergeSort, QuickSort)
* Problem is naturally recursive

#### Use Iteration when:

* Performance is critical
* Deep recursion expected
* Avoiding stack overflow is important

---

> Recursion is more intuitive and cleaner for problems like trees, but iteration is more memory-efficient and safer in production because it avoids stack overflow.

## BFS vs DFS

### Overview

|                | BFS (Breadth-First Search) | DFS (Depth-First Search) |
| -------------- | -------------------------- | ------------------------ |
| Strategy       | Level by level             | Go as deep as possible   |
| Data Structure | Queue (FIFO)               | Stack (LIFO) / Recursion |
| Order          | Wide → Deep                | Deep → Backtrack         |

---

### Traversal Example

#### Tree

```
        A
       / \
      B   C
     / \
    D   E
```

#### BFS

```
A → B → C → D → E
```

#### DFS

##### Pre-order

```
A → B → D → E → C
```

##### In-order (BST only meaningful)

```
D → B → E → A → C
```

#### Post-order

```
D → E → B → C → A
```

---

### Time & Space Complexity

|       | BFS  | DFS  |
| ----- | ---- | ---- |
| Time  | O(n) | O(n) |
| Space | O(n) | O(h) |

※ h = tree height

---

### Advantages

#### BFS

* Finds shortest path (unweighted graph)
* Good for level-order traversal

#### DFS

* Less memory (usually)
* Good for full traversal / backtracking

---

### Disadvantages

#### BFS

* Uses more memory (queue can grow large)

#### DFS

* Can go very deep → stack overflow (recursion)

---

### When to Use

#### Use BFS when:

* Shortest path (unweighted)
* Level-order traversal
* Minimum steps problems

#### Use DFS when:

* Tree traversal (inorder, preorder, postorder)
* Backtracking (permutations, combinations)
* Cycle detection

---

### Implementation

#### BFS

* Use Queue (`deque`)
* Use `popleft()`

#### DFS

* Use Recursion OR Stack
* Traverse deeply first

---

> BFS explores nodes level by level using a queue, while DFS explores as deep as possible using a stack or recursion. BFS is useful for shortest path problems, while DFS is better for full traversal and backtracking.
