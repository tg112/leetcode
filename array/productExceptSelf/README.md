# ProductExceptSelf

### left

`left[i] = left[i - 1] * nums[i - 1]` は  
`left[i] = nums[0] * nums[1] * ... * nums[i - 1]`を表す

### right

`range(start, stop(exclusive), step)` 

`for i in range(len(nums) - 2, -1, -1):` は最後から2番目の要素から開始し、ループごとに-1ずつ減らし、-1になったらループを抜ける。つまり `n - 2 -> 0`


### 文法

`zip`: 同じ index 同士をペアにする

```python
left = [1, 2, 3]
right = [4, 5, 6]

z = zip(left, right)

print(list(z)) # [(1, 4), (2, 5), (3, 6)]
```

`list comprehension`: [式 for 要素 in iterable]

```python
result = [l * r for l, r in zip(left, right)]

# 上下は同じ
result = []

for l, r in zip(left, right):
    result.append(l * r)

```