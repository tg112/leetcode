# Maximum Subarray

**計算量**

- 時間計算量：O(n)
- 空間計算量：O(1)

## Approach
1. We start by initializing two variables: maxSum and currentSum.
    - maxSum represents the maximum sum encountered so far and is initially set to the minimum possible integer value to ensure that any valid subarray sum will be greater than it.
    - currentSum represents the current sum of the subarray being considered and is initially set to 0.
2. We iterate through the nums array using a for loop, starting from the first element and going up to the last element.
3. For each element in the array, we add it to the current sum currentSum. This calculates the sum of the subarray ending at the current element.
4. Next, we check if the current sum currentSum is greater than the current maximum sum maxSum.
    - If it is, we update maxSum with the new value of currentSum. This means we have found a new maximum subarray sum.
5. If the current sum currentSum becomes negative, it indicates that including the current element in the subarray would reduce the overall sum. In such cases, we reset currentSum to 0. This effectively discards the current subarray and allows us to start a fresh subarray from the next element.
6. We repeat steps 3 to 5 for each element in the array.
7. After iterating through the entire array, the variable maxSum will contain the maximum subarray sum encountered.
8. Finally, we return the value of maxSum as the result, representing the maximum sum of a contiguous subarray within the given array nums.