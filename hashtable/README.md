# Hash Table

> A hash table is a data structure that stores key-value pairs and uses a hash function to map keys to indices in an array.

## イメージ

```text
key → hash function → index → value

"apple" → hash → 3 → 800
"banana" → hash → 1 → 1400

配列のインデックスに直接アクセスするので早い
```

## 計算量

| 操作     | 平均   | 最悪   |
| ------ | ---- | ---- |
| insert | O(1) | O(n) |
| search | O(1) | O(n) |
| delete | O(1) | O(n) |

## Hash Function（ハッシュ関数）

> キーを整数（インデックス）に変換する関数

```python
my_hash = (my_hash + ord(letter) * 23) % size
```

### 良いハッシュの条件

- 均等に分散する
- 計算が速い
- 衝突が少ない


## Collision（衝突）

> 異なるキーが同じインデックスにマッピングされること

```python
# 同じ場所に入ってしまう
hash("apple")  → index 2
hash("grape")  → index 2
```

### Collisionの解決法

1. Separate Chaining（分離連鎖法）
    - 各インデックスに「リスト」を持たせる方法
        - 実装が簡単
        - 衝突に強い
2. Open Addressing（オープンアドレッシング）
    - 衝突したら「別の空いている場所」を探す
    - Linear Probing（線形探索）
        - メモリ効率が良い(good)
        - クラスタリンングができる(bad)
        - パフォーマンスが低下(bad)
    ```python
    # index 2 → 埋まってる → index 3 → 空いてる → ここに入れる
    if occupied:
        index = (index + 1) % size

    ```

| 観点      | Separate Chaining | Linear Probing |
| ------- | ----------------- | -------------- |
| 実装      | 簡単                | 少し複雑           |
| メモリ     | 多い                | 少ない            |
| 衝突対応    | リストで保持            | 次の場所へ          |
| パフォーマンス | 安定                | 劣化しやすい         |


> A hash table uses a hash function to map keys to indices. Since collisions can occur, we need strategies to handle them. One common method is separate chaining, where each index stores a list of key-value pairs. Another approach is open addressing, such as linear probing, where we find the next available slot in the array.

### 全体のまとめ

```
key
 ↓
hash function
 ↓
index
 ↓
[ collision発生？ ]
   ↓ YES
   → Separate Chaining（リスト）
   → Linear Probing（次の場所）
```
