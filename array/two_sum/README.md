# TWO Sum

**計算量**

- 時間計算量：O(n)
- 空間計算量：O(n)


## 概要

So the problem is: given an array of integers and a target, I need to return the indices of two numbers such that they add up to the target. I assume there is exactly one solution, and I cannot use the same element twice.

A brute force approach would check all pairs in O(n²), but we can optimize it using a hash map.

I’ll use a dictionary to store previously seen numbers and their indices.　For each number, I compute the complement as target minus the current number.　If the complement is already in the dictionary, I return the indices. Otherwise, I store the current number.

The time complexity is O(n) because we iterate once, and dictionary lookups are O(1) on average. Space complexity is O(n).


`if num_map.get(complement):` Using get() directly can be problematic because index 0 evaluates to False.


Q. なぜ1回のループでいいの？

Because we store previously seen elements, so we don’t need to scan the array again.

Q. なぜdictを使う？

Because it provides O(1) lookup, which reduces time complexity from O(n²) to O(n).




complement: `差分`

## JavaScript

### Map vs Object

#### Object

- キーは 文字列 or Symbolのみ(数値も強制的に文字列になる)
- 順序は保証されない
- パフォーマンス
  - 小規模 & 単純用途なら速い
  - ただしキー数が増えると微妙

```javascript
const obj = {};
obj[1] = "a";

console.log(obj); // { "1": "a" }

// 操作
obj[key] = value;
obj[key];
delete obj[key];
Object.keys(obj).length
```

#### Map

- **どんな型**でもキーにできる
- 挿入順が保証される
- パフォーマンス
  - 大量データで強い
  - 頻繁な追加・削除に向いてる

```javascript
const map = new Map();
map.set(1, "a");

// 操作
map.set(key, value);
map.get(key);
map.has(key);
map.delete(key);
map.size
```

console.log(map.get(1)); // "a"
