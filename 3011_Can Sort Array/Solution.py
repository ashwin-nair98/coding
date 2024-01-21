class Solution:
    def countSetBits(self, num: int) -> int:
        count = 0
        while(num):
            count += num & 1
            num >>= 1
        return count
    
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    # Need to swap
                    if self.countSetBits(nums[j]) == self.countSetBits(nums[j+1]):
                        # Can swap
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                    else:
                        return False
        return True
