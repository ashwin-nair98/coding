class Solution:
    def minimumPushes(self, word: str) -> int:
        heap = [1] * 8
        
        charCounter = Counter(word)
        
        totalCount = 0
        
        for charCount in sorted(charCounter.values(), reverse = True):
            minKey = heappop(heap)
            totalCount += charCount * minKey
            minKey += 1
            heappush(heap, minKey)
        
        return totalCount
