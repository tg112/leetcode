# TWO Sum

**計算量**

- 時間計算量：O(n)
- 空間計算量：O(1)


## 概要

- Two Pointers（双方向ポインタ）の基本パターン
- 「0以外を前に詰める」
  - `left`：次に「非0」を置く位置
  - `right`：配列をスキャンするポインタ


I use a two-pointer approach. The right pointer scans the array, and the left pointer keeps track of the position to place the next non-zero element.
Whenever I find a non-zero value, I swap it with the element at the left pointer and increment the left pointer.
This way, all non-zero elements are moved to the front while maintaining their relative order, and zeros naturally move to the end.
