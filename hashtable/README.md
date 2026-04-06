# HashTable

- Pro 
    - Fast lookups
    - Fast inserts
    - Flexible keys
- Con
    - Unordered
    - Slow key iterations

## Hash function O(1)

任意のデータを「固定サイズの値」に変換する関数

イメージ: `key → hash function → index`

```
"apple" → hash → 980123
"banana" → hash → 234234
```

- 主に以下で使われる
  - HashMap/HashTable
  - データ検索の高速化
  - セキュリティ(パスワードの保存)

  | method | time complexity |
  | --- | --- |
  | search | O(1) |
  | insert | O(1) |
  | lookup | O(1) |
  | delete | O(1) |


**Collision（衝突）**: 異なるキーなのに同じ値になること：

```javascript
class HashTable {
    constructor(size) {
        this.data = new Array(size);
    }

    _hash(key) {
        let hash = 0;
        for (let i = 0; i < key.length; i++) {
            hash = (hash + key.charCodeAt(i) * i) % this.data.length;
        }
        return hash;
    }

    set(key, value) {
        let address = this._hash(key);
        if (!this.data[address]) {
            this.data[address] = [];
        } 
        this.data[address].push([key, value]);
    }

    get(key) {
        const address = this._hash(key);
        const currentBucket = this.data[address];
        if (currentBucket) {
            for (let i = 0; i < currentBucket.length; i++) {
                if (currentBucket[i][0] === key) {
                    return currentBucket[i][1];
                }
            }
        }
        return undefined;
    }

    keys() {
        const keysArray = [];
        for (let i = 0; i < this.data.length; i++>) {
            if (this.data[i]) {
                keyArray.push(this.data[i][0][0]);
            }
        }
        return keysArray;
    }
}

const myHashTable = new HashTable(50);
myHashTable._hash('grapes');
```

```javascript
function firstReccurignChar(nums) {
   const map = {};
   for (let i = 0; i < nums.length; i++) {
       if (map[nums[i]] !== undefined) {
           return nums[i];
       }  else {
       map[nums[i]] = i;
       }
   }
    return undefined;
}
```