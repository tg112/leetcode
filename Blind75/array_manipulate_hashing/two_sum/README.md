# Two Sum

## 問題概要
整数配列 `nums` と整数 `target` が与えられる。合計が `target` となる2つの数のインデックスを返す。  
解は必ず1つ存在し、同じ要素を2回使ってはいけない。

## 計算量
- 時間計算量: O(n) — 1回のループ + O(1) のハッシュマップ参照
- 空間計算量: O(n) — ハッシュマップに最大 n 個の要素を格納

## アプローチ

**Hash Map（辞書）** を使い、ブルートフォース O(n²) を O(n) に改善する。

各要素について:
1. `complement = target - nums[i]` を計算
2. `complement` が辞書に存在すれば → そのインデックスと現在の `i` を返す
3. 存在しなければ → `nums[i]: i` を辞書に登録して次へ

1回のループで済む理由：過去に見た要素を辞書に蓄積しているため、前方を再スキャンする必要がない。

## ポイント

**`map.get(key)` の落とし穴**  
インデックス `0` は Python で `False` と評価されるため、`if map.get(complement)` は `complement` のインデックスが `0` のときに誤って `False` と判定する。  
→ `if complement in map:` を使うのが正しい。

## JavaScript メモ：Map vs Object

| 特性 | Object | Map |
|---|---|---|
| キーの型 | 文字列・Symbol のみ（数値も文字列化） | 任意の型 |
| 挿入順の保証 | なし | あり |
| サイズ取得 | `Object.keys(obj).length` | `map.size` |
| 向いている用途 | 小規模・単純な用途 | 大量データ・頻繁な追加削除 |

```javascript
// Object
const obj = {};
obj[1] = "a";
console.log(obj); // { "1": "a" } ← 数値キーが文字列化される

// Map
const map = new Map();
map.set(1, "a");
console.log(map.get(1)); // "a" ← 数値キーのまま扱える
```
