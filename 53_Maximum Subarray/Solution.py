class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        store = [0] * len(nums)
        store[0] = max(0, nums[0])
        maxSum = max(maxSum, nums[0])
        for i in range(1, len(nums)):
            store[i] = store[i-1] + nums[i]
            maxSum = max(store[i], maxSum)
            store[i] = max(0, store[i])
        return maxSum
