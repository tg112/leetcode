# Recursion

**Recursion = 問題を小さくして自分に任せる**

> Recursion is a technique where a function calls itself to solve a problem.

## 要素

### 1. Base Case（停止条件）

```python
if condition:
    return
# これがないと無限ループ
```

### 2. Recursive Case（再帰呼び出し）

`return func(smaller_input)`  
問題を小さくしていく

## コールスタック（超重要）

**関数の実行履歴を積み上げるスタック**

> The call stack is a data structure that keeps track of function calls. Each time a function is called, it is pushed onto the stack, and when it returns, it is popped off. It follows the LIFO principle and is especially important in recursion.

### 仕組み（超重要）

関数が呼ばれるたびに

1. スタックに積まれる（push）
2.処理が終わると取り出される（pop）


#### イメージ

```
main()
 └── func1()
       └── func2()
```

呼び出し（積む）
```
factorial(3)
factorial(2)
factorial(1)
```

スタック状態
```
[ factorial(1) ]
[ factorial(2) ]
[ factorial(3) ]
```

② 戻る（取り出す）
```
下から戻る（これ重要）
factorial(1) → 1
factorial(2) → 2 * 1 = 2
factorial(3) → 3 * 2 = 6

```

## Iteration（ループ）との違い

|         | Recursion | Loop |
| ------- | --------- | ---- |
| 可読性     | ◎         | △    |
| パフォーマンス | △         | ◎    |
| スタック使用  | あり        | なし   |
