# Given an integer array nums, find the subarray with the largest sum, and return its sum.


# Example 1:
#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:
#
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

# Maximum Subarray(Kadane’s Algorithm)


def maxSubArray(nums: list[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]
    # 2番目の要素からはじめる
    for num in nums[1:]:
        # ①　今の数から新しくスタートする num
        # ② それとも、前の合計に足す
        current_sum = max(num, current_sum + num)
        # 最大値を更新
        max_sum = max(max_sum, current_sum)
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))
