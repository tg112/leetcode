from unittest import result


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        nums_size = len(nums)

        # Store prefix products from the left
        left = [1] * nums_size
        for i in range(1, nums_size):
            left[i] = left[i - 1] * nums[i - 1]


        right = [1] * nums_size

        # Store prefix products from the right
        for i in range(nums_size - 2, -1, -1):
            print(i)
            right[i] = right[i + 1] * nums[i + 1]
        

        # Calculate the result array by multiplying left and right products
        result = [1] * nums_size
        for i in range(nums_size):
            result[i] = left[i] * right[i]
        return result

    def moreEfficient(self, nums: list[int]) -> list[int]:
        n = len(nums)

        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

run = Solution()
print(run.productExceptSelf([1,2,3,4]))