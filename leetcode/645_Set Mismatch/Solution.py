class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        currSum = 0
        seen = set()
        dup = 0

        for i in nums:
            if i in seen:
                dup = i
            else:
                seen.add(i)
            currSum += i
        n = len(nums)
        actualSum = (n * (n + 1))/2
        diff = int(actualSum - currSum)
        return [dup, dup + diff]
