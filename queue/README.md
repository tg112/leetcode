# Queue

**Queueは並ぶ**

> A queue is a data structure that follows the FIFO principle, where the first element added is the first one removed.
> It supports enqueue and dequeue operations, both of which can be implemented in O(1) time using a linked list with front and rear pointers.

```text
[ A ] → [ B ] → [ C ]
  ↑               ↑
dequeue         enqueue
（取り出し）      （追加）


A が最初に並ぶ
A が最初に出る
```

| operation | BigO | explanation |
| --- | --- | --- |
| enqueue | O(1) | 要素を 後ろ（rear / last） に追加 |
| dequeue | O(1) | 要素を 前（front / first） から取り出す |
| peek | O(1) | 一番前の要素を見る（削除しない） |

### よく使う場面

① BFS（超重要）→ グラフ探索
② タスク処理　→ 先に来た仕事から処理
③ バッファ・キュー　→ データの順番を維持


### 実装方法

1. [LinkedList](queue.py) 推奨
2. 配列 (注意が必要)

```python
queue = []
queue.append(1)   # enqueue
# pop(0) は全要素をずらす → O(n)
queue.pop(0)      # dequeue ❌ O(n)

```

#### python実務では下記を使う

```python
from collections import deque

queue = deque()
queue.append(1)     # enqueue
queue.popleft()     # dequeue（O(1)）
```