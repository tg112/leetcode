# Graph

> A graph is a data structure consisting of vertices and edges. It can represent relationships between objects. Graphs can be directed or undirected, and they are commonly implemented using adjacency lists or adjacency matrices.

`「Graphは“関係性”を表すデータ構造」`

## イメージ

```
A —— B
|    /
|   /
C —— D
A, B, C, D → 頂点（vertices）
線 → 辺（edges）
```

## 基本操作

| 操作            | 内容    | 計算量　|
| ------------- | ----- | ------|
| add_vertex    | ノード追加 | O(1) |
| add_edge      | 辺追加   | O(1) |
| remove_edge   | 辺削除   | O(1) |
| remove_vertex | ノード削除 | O(1) |


## グラフの種類

### Undirected Graph（無向グラフ）

```
A —— B
A → B も B → A も同じ
```

### Directed Graph（有向グラフ）

```
A → B
方向がある
```

### Weighted Graph

```
A —(5)— B

edgeに重み（コスト）があ
```

## 表現方法

### Adjacency List（隣接リスト）

- メリット
    - メモリ効率が良い
    - 実務でよく使う

```json
{
  "A": ["B", "C"],
  "B": ["A", "D"],
  "C": ["A", "D"],
  "D": ["B", "C"]
}
```

### Adjacency Matrix（隣接行列）

- メリット
    - 辺の存在チェックが速い（O(1)）
- デメリット
    - メモリを多く使う（O(n²)）

```json
    A B C D
A [ 0 1 1 0 ]
B [ 1 0 0 1 ]
C [ 1 0 0 1 ]
D [ 0 1 1 0 ]
```

