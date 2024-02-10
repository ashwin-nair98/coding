class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1

        if i == 0:
            nums.reverse()
            return
        
        j = len(nums) - 1
        while nums[j] <= nums[i-1]:
            j -= 1


        nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:] = nums[len(nums)-1:i-1:-1]  
