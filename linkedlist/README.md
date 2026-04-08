# Linked List

**Image**

```text
apples
8947 --> grapse (head)
             8742 --> pears
                          372 --> null (tail)
```

### 計算量

| method | 計算量 |
| --- | --- |
| prepend | O(1) |
| append | O(1) |
| lookup | O(n) |
| inseet | O(n) |
| delete | O(n) |

### pointer

- reference to another place of memory


### 1. ノードの本質

```
Node = (value, next)
```

- 配列と違い **連続メモリではない**
- 次の要素は「アドレス（参照）」で辿る

---

### 2. Head / Tail の役割

| 要素 | 意味 |
| --- | --- |
| head | 最初のノード |
| tail | 最後のノード |
| tail.next | 常に `None` |

**head / tail の更新ミスが最もバグを生む**

---

### 3. ポインタ（参照）操作の三原則

```python
after = current.next
current.next = before
before = current
current = after
```

- 参照を失うと復元不可
- 必ず **次を保存してから切り替える**

---

### 4. 境界条件（最重要）

必ず以下を意識する：

- 空リスト
- 要素1個
- 先頭操作（index == 0）
- 末尾操作（index == length - 1）

---

### 5. 時間計算量を言えること

| 操作 | 計算量 |
| --- | --- |
| append (tailあり) | O(1) |
| prepend | O(1) |
| get | O(n) |
| insert (中間) | O(n) |
| remove (中間) | O(n) |
| reverse | O(n) |

※ これを **理由付きで説明できること**

---

### 6. なぜ Python で LinkedList を学ぶのか

- 実務では `list` や `deque` を使う
- **LinkedList はポインタ思考の訓練**
- 木・グラフ・LRU Cache・OS の基礎になる

---

### 7. 面接でよく聞かれるテーマ

- reverse linked list（今回）
- cycle detection（Floyd）
- remove nth from end
- merge two sorted lists
- middle of linked list

---
