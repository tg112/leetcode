# 3 Sum

## Point

-　「重複をいかに効率よく排除するか」と「いかに計算量を $O(N^3)$ から $O(N^2)$ に落とすか」の2点。
-　配列の組み合わせ問題で「重複を許さない」と言われたら、まずは**「最初にソートできないか？」**を考える癖をつけると一気に解法が見えやすくなります。
- `2 pointer`: 基準値 i を固定したあと、残りの探索を left と right の両端から狭めていく手法。**ソート済み配列だからこそ機能する技**で、本来なら残りの2つの探索に $O(N^2)$ かかるところを $O(N)$ に短縮しています。

## Efficient Solution

1. Sort the Array: Begin by sorting the array. This helps in easily skipping over duplicates and using two pointers effectively.

2. Iterate with a Fixed Pointer: Use a loop to fix one number, then apply a two-pointer approach for the remaining sub-array.

3. Two-Pointer Technique: For each fixed element, use two pointers to find the remaining two elements that sum to zero. Start with one pointer at the next element (left), and the other pointer at the end (right) of the array.

4. Check and Adjust Pointers: If the sum of the three elements is zero, add it to the result. If the sum is less than zero, increment the left pointer; if it's greater, decrement the right pointer. This helps in narrowing down the search efficiently.