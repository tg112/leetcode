# Contains Duplicate

## 計算量
時間：O(n)（1回ループ）
空間：O(n)（setに保存）

## 概要

- Hash Set（集合）を使う基本問題
  - すでに見た値かどうかを記録する。すでにみたことある -> 重複
  - 初めて見るなら記憶


The problem asks me to determine whether any value appears at least twice in the array. If so, we return true; otherwise, we return false.

I use a hash set to keep track of the elements I've seen so far.
As I iterate through the array, I check if the current number is already in the set.
If it is, that means we found a duplicate, so I return true.
Otherwise, I add the number to the set and continue.
