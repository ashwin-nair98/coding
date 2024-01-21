class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for i in nums:
            temp = max(prev + i, curr)
            prev = curr
            curr = temp
        return curr
