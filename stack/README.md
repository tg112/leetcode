## Stack(LIFO: Last In First Out)

A stack is a linear data structure that follows the LIFO (Last In, First Out) principle.  
This means: The last element added to the stack is the first one to be removed.  

You can think of a stack like a stack of tennis balls in a can:

- You add balls from the top
- You remove balls from the top

So,

 only the top element is accessible.

```text
イメージは上に重ねていくイメージ

   ↑ 一番上を取り出す（pop）
   　 
     ↓-- peek(覗く)
 │  ⚾  │ ← top（最後に入れた）
 │  ⚾  │
 │  ⚾  │ ← bottom（最初に入れた）
 └─────-┘
   ↓ 上に積むイメージ（push）
```

### よく使われる場面

1. DFS
2. Undo
3. 括弧チェック 

### 計算量

| operation |　bigO |
| --- | --- |
| push | O(1) |
| pop  | O(1) |
| peek | O(1) |


### 実装方法

1. 配列(実務でよく使う)

```python
stack = []
stack.append(1) # push
stack.pop()     # pop
```

2. LinkedList(メリットは、サイズ制限なし・push/popが確実にO(1))

[stack.pyを参照](./stack.py)


| 観点       | 配列            | Linked List |
| --------  | ------------- | ----------- |
| 実装の簡単さ   | ◎             | △           |
| push/pop     | O(1)（アモータイズド） | O(1)（確実）    |
| メモリ効率     | ◎             | ❌           |
| パフォーマンス  | ◎（実務では速い）     | △           |
| 柔軟性        | △             | ◎           |


> LinkedListでの開発において、メモリ効率が悪くなる主な理由は、
> 各ノードが「値 + ポインタ」を持つ追加コストがあるから。

In practice, stacks are usually implemented using arrays because they are simpler and more cache-friendly, which makes them faster in most cases.
However, a linked list implementation guarantees O(1) time for push and pop without resizing, so it’s useful to understand both approaches.

Even though array resizing is O(n), it happens infrequently, so the amortized time complexity is still O(1).